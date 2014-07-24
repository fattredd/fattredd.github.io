#include <cstdio>
#include <stdlib.h>
#include <GL/glew.h>
#include <GL/glut.h>

static GLuint make_texture(const char *filename){
	GLuint texture;
	int width, height;
	void *pixels = read_tga(filename,&width,&height);
	if (!pixels) return 0;
}

static const GLfloat g_vertex_buffer_data[]={
	-1.0f,-1.0f,
	1.0f,-1.0f,
	-1.0f,1.0f,
	1.0f,1.0f
};
static const GLushort g_element_buffer_data[]={0,1,2,3};

static struct {
	GLuint vertex_buffer, element_buffer;
	GLuint textures[2];
} g_resources;

static GLuint make_buffer(GLenum target,
		const void*buffer_data,
		GLsizei buffer_size){
	GLuint buffer;
	glGenBuffers(1,&buffer);
	glBindBuffer(target,buffer);
	glBufferData(target,buffer_size,buffer_data,GL_STATIC_DRAW);
	return buffer;
}

static int make_resources(void) {
	g_resources.vertex_buffer = make_buffer(
		GL_ARRAY_BUFFER,
		g_vertex_buffer_data,
		sizeof(g_vertex_buffer_data));
	g_resources.element_buffer = make_buffer(
                GL_ELEMENT_ARRAY_BUFFER,
                g_element_buffer_data,
                sizeof(g_element_buffer_data));
}

static void update_fade_factor(void) {

}

static void render(void) {
	glClearColor(1.0f,1.0f,1.0f,1.0f);
	glClear(GL_COLOR_BUFFER_BIT);
	glutSwapBuffers();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE);
	glutInitWindowSize(400,300);
	glutCreateWindow("Hello World");
	glutDisplayFunc(&render);
	glutIdleFunc(&update_fade_factor);
	glewInit();
	if (!make_resources) {
		fprintf(stderr,"failed to load resources\n");
		return 1;
	}

	glutMainLoop();
	return 0;
}
