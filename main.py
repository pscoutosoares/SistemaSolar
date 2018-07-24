import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(1,-1,-1),
	(1,1,-1),
	(-1,1,-1),
	(-1,-1,-1),
	(1,-1,1),
	(1,1,1),
	(-1,-1,1),
	(-1,1,1)
)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
)

superficies = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(4,0,3,6)
)

colors = (
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0.4),
	(1,0,1),
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0.4),
	(1,0,1),
	(1,1,1),
	(1,0.4,1)
)
def Cube():
	glBegin(GL_QUADS)
	x = 0
	for face in superficies:
		x+=1
		#adiciona cor a superficie
		
		for vertex in face:
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()



	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()


def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

	#maxima distancia que será renderizada
	gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
	#perspectiva de visão na tela (x,y,z)
	glTranslatef(0.0,0.0,-5)
	#rotação
	glRotatef(20,20,3,0)


	i,j,k = 0,0,0
	#Mantem o código rodando
	while True:
		for event in pygame.event.get():
			#Se o usuário fechar a caixa de execução o programa chama a função pygame.quit()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1,0,0)

				if event.key == pygame.K_RIGHT:
					glTranslatef(1,0,0)

				if event.key == pygame.K_UP:
					glTranslatef(0,1,0)

				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1.0)
				if event.button == 5:
					glTranslatef(0,0,-1.0)



		#glRotatef(1,2,3,2)
		#limpar o cache de cor e profundidade
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		#atualiza o display com flip (flip>update)
		pygame.display.flip()
		#10 ms por frame
		pygame.time.wait(10)

main()