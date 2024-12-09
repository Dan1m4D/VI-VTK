from vtkmodules.all import *

def render_plane(textureFile="P2/images/lena.JPG"):
    planeSource = vtkPlaneSource()
    planeSource.SetCenter(0, 0, 0)
    planeSource.SetResolution(100, 100)
    # planeSource.SetOrigin(0, 0, 0)
    # planeSource.SetPoint1(20, 30, 0)
    # planeSource.SetPoint2(0, 80, 40)


    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(planeSource.GetOutputPort())

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)

    # Get a jpeg texture
    jpegReader = vtkJPEGReader()
    jpegReader.SetFileName(textureFile)
    jpegReader.Update()

    # Create a texture object
    texture = vtkTexture()
    texture.SetInputConnection(jpegReader.GetOutputPort())

    planeActor.SetTexture(texture)

    return planeActor

def main():
    planeActor = render_plane()

    ren = vtkRenderer()
    ren.AddActor(planeActor)
    ren.SetBackground(0.1, 0.2, 0.3)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(600, 600)
    renWin.SetWindowName("T E X T U R E S")

    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

if __name__ == "__main__":
    main()