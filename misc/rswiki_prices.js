// ==UserScript==
// @name         RSwiki Price buyin
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Show the total cost to buy as many as possible
// @author       fattredd
// @match        https://prices.runescape.wiki/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=runescape.wiki
// ==/UserScript==
'use strict';

var ourClass = "buyin";
var ourParentClass = "parentBuyin";
var newRowHolder = {};
var newColHolder = [];
var newColList = [];
var newURL;
var observer = new MutationObserver(()=>{});

// Define the rows we'd like to add
makeRow("All In", () => {
    // Total cost to buy up to limit
    let sellPrice = Number(document.getElementsByClassName("wgl-item-price")[1].textContent.split(" ")[0].replace(",",""));
    let buyLimitSection = document.getElementsByClassName("wgl-item-details-table")[0].childNodes[0];
    let buyLimit = Number(buyLimitSection.childNodes[0].childNodes[1].textContent.replace(",",""));
    let result = sellPrice * buyLimit;
    return result.toLocaleString("en-US");
});
makeRow("All Out", () => {
    // Total cost to sell all those items
    let buyPrice = Number(document.getElementsByClassName("wgl-item-price")[0].textContent.split(" ")[0].replace(",",""));
    let buyLimitSection = document.getElementsByClassName("wgl-item-details-table")[0].childNodes[0];
    let buyLimit = Number(buyLimitSection.childNodes[0].childNodes[1].textContent.replace(",",""));
    let tax = Math.floor(buyPrice * 0.01);
    let result = (buyPrice - tax) * buyLimit;
    return result.toLocaleString("en-US");
});
makeRow("Act Prof", () => {
    // Actual profit including tax
    let buyPrice = Number(document.getElementsByClassName("wgl-item-price")[0].textContent.split(" ")[0].replace(",",""));
    let sellPrice = Number(document.getElementsByClassName("wgl-item-price")[1].textContent.split(" ")[0].replace(",",""));
    let buyLimitSection = document.getElementsByClassName("wgl-item-details-table")[0].childNodes[0];
    let buyLimit = Number(buyLimitSection.childNodes[0].childNodes[1].textContent.replace(",",""));
    let tax = Math.floor(buyPrice * 0.01);
    let result = (buyPrice - sellPrice - tax) * buyLimit;
    return result.toLocaleString("en-US");
});

function makeRow(title, updateFunc) {
    var newRow = document.createElement('tr');
    newRow.class=ourClass;
    let titleTd = document.createElement('td');
    titleTd.textContent=title;
    titleTd.class=ourClass;
    let descTd = document.createElement('td');
    descTd.textContent="loading...";
    descTd.class=ourClass;
    newRow.appendChild(titleTd);
    newRow.appendChild(descTd);
    newRowHolder[title] = {"elem":newRow, "func": updateFunc};
};
function initRows() {
    // Create add our rows to the page
    var parent = document.getElementsByClassName("wgl-item-details-table")[0].childNodes[0];
    Object.entries(newRowHolder).forEach(([title, data]) => {
        parent.appendChild(data.elem);
    });
}
function updateRows() {
    // Update existing rows
    Object.entries(newRowHolder).forEach(([title, data]) => {
        data.elem.childNodes[1].textContent = data.func();
    });
}

function setupCols() {
    newColList = [];
    makeColEquation(8, async (rowNum) => { // Margin
        let buyPrice = Number(getCol(4, rowNum, 1, true));
        let sellPrice = Number(getCol(6, rowNum, 1, true));
        let margin = buyPrice - sellPrice;
        let tax = Math.floor(buyPrice * 0.01);
        let realMargin = margin - tax;
        //console.log(`margin: ${rowNum}: ${buyPrice} ${margin} ${tax}, ${realMargin}`);
        let result = new Intl.NumberFormat('en-US').format(realMargin);
        return `(${result})\n`;
    });
    makeColEquation(10, async (rowNum) => { // Profit
        let buyLimit = Number(getCol(2, rowNum, 1, true));
        let buyPrice = Number(getCol(4, rowNum, 1, true));
        let sellPrice = Number(getCol(6, rowNum, 1, true));
        let margin = buyPrice - sellPrice;
        let tax = Math.floor(buyPrice * 0.01);
        let realMargin = margin - tax;
        let realProfit = buyLimit * realMargin;
        //console.log(`profit: ${rowNum}: ${buyLimit}, ${buyPrice} ${sellPrice}, ${tax}, ${realProfit}`);
        let result = new Intl.NumberFormat('en-US').format(realProfit);
        return `(${result})\n`;
    });
};
function makeColEquation(colNum, updateFunc){
    newColList.push(colNum);
    let colCount = getCol(-1,0,1);
    for (let i=0; i<colCount; i++) {
        let parentCell = getCol(colNum, i, 1);
        makeColInsert(parentCell, i, updateFunc);
    }
}

async function makeColInsert(parent, rowNum, updateFunc) {
    if (!parent.classList.contains(ourParentClass)) parent.classList.add(ourParentClass);
    if (parent.childNodes[0].class == ourClass) parent.childNodes[0].remove();
    let colIns = document.createElement('span');
    colIns.textContent="(?)\n";
    colIns.class=ourClass;
    parent.prepend(colIns);
    let newCol = {"elem":colIns, "rowNum":rowNum, "func": updateFunc};
    newColHolder.push(newCol);
}
function getCol(colNum=0, rowNum=0, tIndex=0, retText=false) {
    // colNum is the column number, <0 to return number of rows
    // tIndex is 0 for header, 1 for body
    //                                                                table - thead/tbody -     tr
    let node = document.getElementsByClassName("wgl-allitemstable")[0].childNodes[tIndex].childNodes;
    if (colNum < 0) return node.length;
    // TODO: handle changing table length
    let row = node[rowNum].childNodes;
    let out = row[colNum];
    let cellLastChild = out.childNodes.length-1;
    if (retText) out = out.childNodes[cellLastChild].textContent.replace(",","");
    //console.log(`getCol: ${colNum}, ${rowNum}, ${retText}, ${out}`);
    return out;
}
function updateCols() {
    // Update existing rows
    newColHolder.forEach((data) => {
        let newVal = data.func(data.rowNum)
        Promise.resolve(newVal).then((value) => {
            data.elem.textContent = value;
        })
    });
}

var observeDOM = (function(){
  // Stolen from here: https://stackoverflow.com/questions/3219758/detect-changes-in-the-dom
  var MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
  return function( obj, callback ){
    if( !obj || obj.nodeType !== 1 ) return;
    if( MutationObserver ){
      var mutationObserver = new MutationObserver(callback)
      mutationObserver.observe( obj, { childList:true, subtree:true })
      return mutationObserver
    }
    else if( window.addEventListener ){
      obj.addEventListener('DOMSubtreeModified', callback, false)
    }
  }
})();

setInterval(() => {
    // Check if we need to init based on the page url
    if (String(window.location) != newURL) {
        newURL = String(window.location);
        let itemPageRegex = /\/item\/\d+$/;
        let allItemsPageRegex = /\/(all-items)|(favourites)$/;
        if (String(newURL).match(itemPageRegex)) {
            // New page is an item page
            setTimeout(initRows, 100);

            // Set up a new DOM observer
            var mainBody = document.getElementsByClassName("wgl-page-container")[0];
            observer = observeDOM(mainBody, (mutationList, observer) => {
                // If we're on a new URL, remove the old observer
                if (String(window.location) != newURL) {
                    observer.disconnect();
                    return;
                }

                // Determine if the DOM changed because of us, or from something else
                for (const mutation of mutationList) {
                    if (mutation.type === 'childList' && mutation.target.class != ourClass) {
                        // Update our values if something else has changed
                        setTimeout(updateRows, 100);
                        return;
                    }
                }
            });
        } else if (String(newURL).match(allItemsPageRegex)) {
            // Set up a new DOM observer
            console.log(`Setting observer for allItems`);
            setTimeout(setupCols, 200);
            setTimeout(updateCols, 300);

            var mainBody2 = document.getElementsByClassName("wgl-page-container")[0];
            observer = observeDOM(mainBody2, (mutationList, observer) => {
                // If we're on a new URL, remove the old observer
                if (String(window.location) != newURL) {
                    observer.disconnect();
                    return;
                }

                // Determine if the DOM changed because of us, or from something else
                for (const mutation of mutationList) {
                    let rmNodes = mutation.removedNodes.item(0);
                    if (mutation.type === 'childList' &&
                        ! mutation.target.classList.contains(ourParentClass) &&
                        rmNodes == null &&
                        mutation.target.class != ourClass) {
                        // Update our values if something else has changed

                        setTimeout(setupCols, 100);
                        setTimeout(updateCols, 300);
                        return;
                    }
                }
            });
        }
    }
}, 1000);
