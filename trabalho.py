import bpy
import mathutils

# especificar a pasta onde esta localizado o trabalho
pastaRaizTrabalho = "C:\\Users\\Suarez\\Desktop\\trabalhoCasa\\"

def constroiModelo():
    constroiJardim()

    constroiCasa()

def constroiJardim():
    cor = getCorVerde()
    
    constroiPlano([(0,0,0),(0,3,0),(3,3,0),(3,0,0)], cor, "Jardim1")

    constroiPlano([(0, 3, 0), (3, 3, 0), (3, 6, 0), (0, 6, 0)], cor, "Jardim2")

def constroiCasa():
    constroiParteDaFrenteDaCasa()

    constroiParteTraseiraDaCasa()

    constroiParteLateralDaCasa()

    constroiParteSuperiorDaCasa()

    constroiParteInferiorDaCasa()

def constroiParteDaFrenteDaCasa():
    constroiPortaDaFrenteDaCasa()
    constroiParedeDaFrenteDaCasa()

def constroiPortaDaFrenteDaCasa():
    constroiCubo(getVerticesPortaDaFrenteDaCasa(), getCorMarrom(), "PortaDaFrente")

def getVerticesPortaDaFrenteDaCasa():
    ma = 0.05
    b = 2.1
    c = 0.011

    return [(4 + ma, 0,0 ),(4 + ma, c, 0),(5 - ma,c,0),(5 - ma, 0, 0), (4 + ma, 0, b), (4 + ma, c, b), (5 - ma, c, b), (5 - ma, 0, b)]

def constroiParedeDaFrenteDaCasa():
    constroiPersonalizado(getVerticesParedeDaFrenteDaCasa(), [(0, 4, 5, 6, 7, 8, 9, 3)], getCorAzul(), "ParedeDaFrente")

    

def getVerticesParedeDaFrenteDaCasa():
    na = 0.040
    
    return [(3,0,0), (3,3,0), (3,3,3), (3,0,3), (4+na,0,0), (4+na,0,2.11), (5-na,0,2.11), (5-na,0,0), (6,0,0), (6,0,3), (6,3,3), (6,3,0)]

def constroiParteTraseiraDaCasa():
    constroiParedeTraseiraDaCasa()

def constroiParedeTraseiraDaCasa():
    constroiPlano([(6, 6, 0), (6, 6, 3), (3, 6, 3), (3, 6, 0)], getCorAzul(), "ParedeTraseira1")

def constroiParteLateralDaCasa():
    constroiParteLateralDireitaDaCasa()
    constroiParteLateralEsquerdaDaCasa()

def constroiParteLateralDireitaDaCasa():
    constroiParedeLateralDireitaDaCasa()

def constroiParedeLateralDireitaDaCasa():
    constroiPersonalizado(getVerticesParedeDaFrenteDaCasa(), [(11, 8, 9, 10)], getCorAzul(), "ParedeLateralDireita1")

    constroiPlano([(6, 3, 0), (6, 6, 0), (6, 6, 3), (6, 3, 3)], getCorAzul(), "ParedeLateralDireita2")
    
def constroiParteLateralEsquerdaDaCasa():
    constroiParedeLateralEsquerdaDaCasa()

    constroiJanelaLateralEsquerdaDaCasa()

def constroiParedeLateralEsquerdaDaCasa():
    constroiPersonalizado(getVerticesParedeDaFrenteDaCasa(), [(0, 3, 2, 1)], getCorAzul(), "ParedeLateralEsquerda1")
    
    constroiPersonalizado([(3, 5, 1), (3, 5, 2), (3, 4, 2), (3, 4, 1), (3, 6, 0), (3, 6, 3), (3, 3, 3), (3, 3, 0)], [(4, 0, 3, 7), (7, 3, 2, 6), (6, 2, 1, 5), (5, 1, 0, 4)], getCorAzul(), "ParedeLateralEsquerda2ComJanela")

def constroiJanelaLateralEsquerdaDaCasa():
    constroiPersonalizadoComFrame([(3, 5, 1), (3, 5, 2), (3, 4, 2), (3, 4, 1) ], [(0, 1, 2, 3)], getCorAzul(), "JanelaLateralEsquerda")

def constroiParteSuperiorDaCasa():
    constroiTelhado()

    constroiTelhas()

def constroiTelhado():
    cor = getCorMarrom()
    
    constroiPersonalizado([(3, 0, 3), (4.5, 0, 4), (6, 0, 3) ], [(1, 2, 0)], cor, "Telhado1")

    constroiPersonalizado([(3, 6, 3), (4.5, 6, 4), (6, 6, 3) ], [(1, 2, 0)], cor, "Telhado2")

def constroiTelhas():
    cor = getCorMarrom()
    
    constroiPersonalizado([(3, 0, 3), (4.5, 0, 4), (4.5, 6, 4), (3, 6, 3)], [(0, 1, 2, 3)], cor, "Telhas1")

    constroiPersonalizado([(6, 0, 3), (4.5, 0, 4), (4.5, 6, 4), (6, 6, 3)], [(0, 1, 2, 3)], cor, "Telhas2")

def constroiParteInferiorDaCasa():
    cor = getCorMarrom()
    
    constroiPlano([(3, 0, 0), (3, 3, 0), (6, 3, 0), (6, 0, 0)], cor, "piso1")

    constroiPlano([(6, 3, 0), (6, 6, 0), (3, 6, 0), (3, 3, 0)], cor, "piso2")

    constroiPlano([(3, 0, 3), (3, 3, 3), (6, 3, 3), (6, 0, 3)], cor, "terraco1")

    constroiPlano([(6, 3, 3), (6, 6, 3), (3, 6, 3), (3, 3, 3)], cor, "terraco2")

def constroiPlano(vertices, cor, nome):
    constroiMalha('Plane', cor, vertices, [(0,1,2,3)], False, nome)
    
def constroiCubo(vertices, cor, nome):
    constroiMalha('Cube', cor, vertices, [(0,1,2,3), (4,5,6,7), (0,4,7,3), (0,1,5,4), (1,2,6,5), (7,6,2,3)], False, nome)
        
def constroiPersonalizado(vertices, faces, cor, nome):
    constroiMalha('Custom', cor, vertices, faces, False, nome)
    
def constroiPersonalizadoComFrame(vertices, faces, cor, nome):
    constroiMalha('Frame', cor, vertices, faces, True, nome)

def constroiMalha(tipo, cor, vertices, faces, comFrame, nome):
    malha = bpy.data.meshes.new(nome);
    malha.from_pydata(vertices, [], faces)
    malha.update()
    
    object = bpy.data.objects.new(nome, malha)
    atribuiCor(object, cor, nome)

    if comFrame :
        object.modifiers.new("frameForm", 'WIREFRAME')
    
    view_layer = bpy.context.view_layer
    view_layer.active_layer_collection.collection.objects.link(object)

def atribuiCor(object, cor, nome):
    material = bpy.data.materials.new(name = nome)
    material.use_nodes = True
    
    imagem = material.node_tree.nodes.new('ShaderNodeTexImage')
    imagem.image = bpy.data.images.load(cor)
    
    material.node_tree.links.new(material.node_tree.nodes["Principled BSDF"].inputs['Base Color'], imagem.outputs['Color'])
    
    if object.data.materials:
        object.data.materials[0] = material
    else:
        object.data.materials.append(material)
    
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
    
    removeCameras()

    criaLuzes(objetoCenario)

    criaCameras(cenario, objetoCenario)

    renderizaVistas(cenario)

def ajustaConfiguracaoCenario():
    configuracao = bpy.data
    
    configuracao.scenes[0].render.resolution_x = 3840
    configuracao.scenes[0].render.resolution_y = 2160

def removeCameras():
    bpy.ops.object.select_all(action = 'DESELECT')
    bpy.ops.object.select_by_type(type = 'CAMERA')
    bpy.ops.object.delete()
    bpy.ops.object.select_by_type(type = 'LIGHT')
    bpy.ops.object.delete()

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
    criaCamera(cenario, objetoCenario, mathutils.Vector((3, 19, 2.5)), mathutils.Euler((48.69, 135.09, 0)), "CameraTraseira")
    criaCamera(cenario, objetoCenario, mathutils.Vector((3, 3, 20)), mathutils.Euler((0, 0, 0)), "CameraSuperior")
    criaCamera(cenario, objetoCenario, mathutils.Vector((3, -13, 2.5)), mathutils.Euler((-48.69, 0, 0)), "CameraFrontal")
    criaCamera(cenario, objetoCenario, mathutils.Vector((19, 3, 2.2)), mathutils.Euler((190.09, 0, -48.69)), "CameraLateralDireita")
    criaCamera(cenario, objetoCenario, mathutils.Vector((-13, 3, 2.2)), mathutils.Euler((190.09, 0, 48.69)), "CameraLateralEsquerda")

def criaCamera(cenario, objetoCenario, localizacao, rotacao, nome):
    camera = bpy.data.cameras.new(nome)
    objetoCamera = bpy.data.objects.new(nome, camera)
    objetoCenario.objects.link(objetoCamera)
    cenario.camera = objetoCamera
    objetoCamera.location = localizacao
    objetoCamera.rotation_euler =  rotacao

def renderizaVistas(cenario):
    vistaAtual = 0

    nomeVista = ['Traseira', 'Superior', 'Frontal', 'LateralDireita', 'LateralEsquerda']

    for objeto in cenario.objects:
        if objeto.type == 'CAMERA':
            renderizaVistaCamera(objeto, cenario, pastaRaizTrabalho + "vistas\\vista" + nomeVista[vistaAtual])
            vistaAtual += 1

def renderizaVistaCamera(objeto, cenario, nomeArquivoVista):
    bpy.context.scene.camera = objeto
    cenario.render.filepath = nomeArquivoVista
    bpy.ops.render.render(write_still= True) 

constroiModelo()

renderizaModelo()
    

