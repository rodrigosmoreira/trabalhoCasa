import bpy
import mathutils

# especificar a pasta onde esta localizado o trabalho
pastaRaizTrabalho = "C:\\Users\\Suarez\\Desktop\\trabalhoCasa\\"

def constroiModelo():
    constroiJardim()

    constroiCasa()

def constroiJardim():
    cor = getCorVerde()
    
    constroiPlano([(0,0,0),(0,6,0),(3,6,0),(3,0,0)], cor, "Jardim")

def constroiCasa():
    constroiParteDaFrenteDaCasa()

    constroiParteTraseiraDaCasa()

    constroiParteLateralDaCasa()

    constroiTelhadoDaCasa()

    constroiPisoDaCasa()

def constroiParteDaFrenteDaCasa():
    constroiPortaDaFrenteDaCasa()
    constroiParedeDaFrenteDaCasa()

def constroiPortaDaFrenteDaCasa():
    constroiCubo([(4.05, 0, 0), (4.05, 0.011, 0), (4.95, 0.011, 0), (4.95, 0, 0), (4.05, 0, 2.1), (4.05, 0.011, 2.1), (4.95, 0.011, 2.1), (4.95, 0, 2.1)], getCorMarrom(), "PortaDaFrente")

def constroiParedeDaFrenteDaCasa():
    constroiPersonalizado([(3, 0, 0), (3, 3, 0), (3, 3, 3), (3, 0, 3), (4.04, 0, 0), (4.04, 0, 2.11), (4.96, 0, 2.11), (4.96, 0, 0), (6, 0, 0), (6, 0, 3), (6, 3, 3), (6, 3, 0)], [(0, 4, 5, 6, 7, 8, 9, 3)], getCorAzul(), "ParedeDaFrente")

    constroiPersonalizado([(3, 0, 3), (4.5, 0, 4), (6, 0, 3) ], [(1, 2, 0)], getCorAzul(), "ParedeDaFrenteTelhado")

def constroiParteTraseiraDaCasa():
    constroiParedeTraseiraDaCasa()

def constroiParedeTraseiraDaCasa():
    constroiPlano([(6, 6, 0), (6, 6, 3), (3, 6, 3), (3, 6, 0)], getCorAzul(), "ParedeTraseira")
    
    constroiPersonalizado([(3, 6, 3), (4.5, 6, 4), (6, 6, 3) ], [(1, 2, 0)], getCorAzul(), "ParedeTraseiraTelhado")

def constroiParteLateralDaCasa():
    constroiParteLateralDireitaDaCasa()
    constroiParteLateralEsquerdaDaCasa()

def constroiParteLateralDireitaDaCasa():
    constroiParedeLateralDireitaDaCasa()

def constroiParedeLateralDireitaDaCasa():
    constroiPlano([(6, 0, 0), (6, 6, 0), (6, 6, 3), (6, 0, 3)], getCorAzul(), "ParedeLateralDireita")
    
def constroiParteLateralEsquerdaDaCasa():
    constroiParedeLateralEsquerdaDaCasa()

    constroiJanelaEsquerdaDaCasa()

def constroiParedeLateralEsquerdaDaCasa():
    constroiPersonalizado([(3, 3, 1), (3, 3, 2.2), (3, 1, 2.2), (3, 1, 1), (3, 6, 0), (3, 6, 3), (3, 0, 3), (3, 0, 0)], [(4, 0, 3, 7), (7, 3, 2, 6), (6, 2, 1, 5), (5, 1, 0, 4)], getCorAzul(), "ParedeLateralEsquerda")

def constroiJanelaEsquerdaDaCasa():
    constroiPersonalizadoComFrame([(3, 3, 1), (3, 3, 2.2), (3, 1, 2.2), (3, 1, 1) ], [(0, 1, 2, 3)], getCorAzul(), "JanelaEsquerda")

def constroiTelhadoDaCasa():
    cor = getCorMarrom()
    
    constroiPersonalizado([(3, 0, 3), (4.5, 0, 4), (4.5, 6, 4), (3, 6, 3)], [(0, 1, 2, 3)], cor, "TelhadoEsquerda")

    constroiPersonalizado([(6, 0, 3), (4.5, 0, 4), (4.5, 6, 4), (6, 6, 3)], [(0, 1, 2, 3)], cor, "TelhadoDireita")

def constroiPisoDaCasa():
    cor = getCorMarrom()
    
    constroiPlano([(3, 0, 0), (3, 6, 0), (6, 6, 0), (6, 0, 0)], cor, "Piso")

    constroiPlano([(3, 0, 3), (3, 6, 3), (6, 6, 3), (6, 0, 3)], cor, "Terraco")

def constroiPlano(vertices, cor, nome):
    constroiMalha('Plane', cor, vertices, [(0,1,2,3)], False, nome)
    
def constroiCubo(vertices, cor, nome):
    constroiMalha('Cube', cor, vertices, [(0,1,2,3), (4,5,6,7), (0,4,7,3), (0,1,5,4), (1,2,6,5), (7,6,2,3)], False, nome)
        
def constroiPersonalizado(vertices, faces, cor, nome):
    constroiMalha('Custom', cor, vertices, faces, False, nome)
    
def constroiPersonalizadoComFrame(vertices, faces, cor, nome):
    constroiMalha('Frame', cor, vertices, faces, True, nome)

def constroiMalha(tipo, cor, vertices, faces, comFrame, nome):
    bpy.context.view_layer.active_layer_collection.collection.objects.link(criaObjetoComMalha(tipo, cor, vertices, faces, comFrame, nome))

def criaObjetoComMalha(tipo, cor, vertices, faces, comFrame, nome):
    objeto = bpy.data.objects.new(nome, criaMalha(nome, vertices, faces))
    
    atribuiCor(objeto, cor, nome)

    if comFrame :
        objeto.modifiers.new("frameForm", 'WIREFRAME')

    return objeto

def criaMalha(nome, vertices, faces):
    malha = bpy.data.meshes.new(nome);
    malha.from_pydata(vertices, [], faces)
    malha.update()

    return malha

def atribuiCor(objeto, cor, nome):
    material = criaMaterialComCor(nome, cor)
    
    if objeto.data.materials:
        objeto.data.materials[0] = material
    else:
        objeto.data.materials.append(material)

def criaMaterialComCor(nome, cor):
    material = bpy.data.materials.new(name = nome)
    material.use_nodes = True
    material.node_tree.links.new(material.node_tree.nodes["Principled BSDF"].inputs['Base Color'], criaCor(cor, material))

    return material

def criaCor(cor, material):
    corMaterial = material.node_tree.nodes.new('ShaderNodeTexImage')
    corMaterial.image = bpy.data.images.load(cor)

    return corMaterial.outputs['Color']
    
def getCorVerde():
    return  pastaRaizTrabalho + "\\cores\\verde.png"

def getCorMarrom():
    return  pastaRaizTrabalho + "\\cores\\marrom.png"

def getCorAmarelo():
    return  pastaRaizTrabalho + "\\cores\\amarelo.png"

def getCorCinza():
    return  pastaRaizTrabalho + "\\cores\\cinza.png"

def getCorAzul():
    return  pastaRaizTrabalho + "\\cores\\azul.png"

def renderizaModelo():
    cenario = bpy.context.scene
    objetoCenario = bpy.context.collection

    ajustaConfiguracaoCenario()

    criaLuzes(objetoCenario)

    criaCameras(cenario, objetoCenario)
    
    renderizaVistas(cenario)

def ajustaConfiguracaoCenario():
    configuracao = bpy.data
    
    configuracao.scenes[0].render.resolution_x = 3840
    configuracao.scenes[0].render.resolution_y = 2160

def criaLuzes(objetoCenario):
    criaLuz(1500, (-5, 3, 8), objetoCenario, "LuzLateralEsquerda")
    criaLuz(500, (2, 2, 8), objetoCenario, "LuzSuperior")
    criaLuz(500, (10, 2, 8), objetoCenario, "LuzLateralDireita")
    criaLuz(300, (3, -5, 8), objetoCenario, "LuzFrontal")
    criaLuz(300, (3, 10, 8), objetoCenario, "LuzTraseira")

def criaLuz(energia, localizacao, objetoCenario, nome):
    luz = bpy.data.lights.new(name=nome, type='POINT')
    luz.energy = energia
    objetoLuz = bpy.data.objects.new(name = nome, object_data = luz)
    objetoCenario.objects.link(objetoLuz)
    bpy.context.view_layer.objects.active = objetoLuz
    objetoLuz.location = localizacao

def criaCameras(cenario, objetoCenario):
    criaCamera(cenario, objetoCenario, mathutils.Vector((3, 22, 2.5)), mathutils.Euler((48.69, 135.09, 0)), "Traseira")
    criaCamera(cenario, objetoCenario, mathutils.Vector((3, 3, 23)), mathutils.Euler((0, 0, 0)), "Superior")
    criaCamera(cenario, objetoCenario, mathutils.Vector((3, -16, 2.5)), mathutils.Euler((-48.69, 0, 0)), "Frontal")
    criaCamera(cenario, objetoCenario, mathutils.Vector((22, 3, 2.2)), mathutils.Euler((190.09, 0, -48.69)), "LateralDireita")
    criaCamera(cenario, objetoCenario, mathutils.Vector((-16, 3, 2.2)), mathutils.Euler((190.09, 0, 48.69)), "LateralEsquerda")
    criaCamera(cenario, objetoCenario, mathutils.Vector((-10, -10, 10)), mathutils.Euler((20, 0, 150.02)), "EmPerspectiva")

def criaCamera(cenario, objetoCenario, localizacao, rotacao, nome):
    camera = bpy.data.cameras.new(nome)
    objetoCamera = bpy.data.objects.new(nome, camera)
    objetoCenario.objects.link(objetoCamera)
    cenario.camera = objetoCamera
    objetoCamera.location = localizacao
    objetoCamera.rotation_euler =  rotacao

def renderizaVistas(cenario):
    for objeto in cenario.objects:
        if objeto.type == 'CAMERA':
            renderizaVistaCamera(objeto, cenario)

def renderizaVistaCamera(camera, cenario):
    bpy.context.scene.camera = camera
    cenario.render.filepath = pastaRaizTrabalho + "vistas\\vista" +  camera.name
    bpy.ops.render.render(write_still= True) 

constroiModelo()

renderizaModelo()
    

