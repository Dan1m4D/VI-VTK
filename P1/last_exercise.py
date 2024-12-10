from vtkmodules.all import *

def render_main_cone():
    """Renders the main sphere in the center of the scene."""
    coneSource = vtkConeSource()
    coneSource.SetCenter(0.5, 0.0, 0.5)
    coneSource.SetHeight(2.0)
    coneSource.SetRadius(1.0)
    coneSource.SetResolution(100)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(coneSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    return sphereActor

def createLightWithSphere(renderer, color, position):
    """
    Creates a light of the given color and position, and adds a sphere to represent it.
    The sphere will not be affected by other lights.
    """
    # Create the light
    light = vtkLight()
    light.SetColor(color)
    light.SetPosition(position)
    light.SetFocalPoint(0.0, 0.0, 0.0)  # All lights point towards the origin
    renderer.AddLight(light)

    sphereSource = vtkSphereSource()
    sphereSource.SetCenter(position)
    sphereSource.SetRadius(0.5)
    sphereSource.SetPhiResolution(50)
    sphereSource.SetThetaResolution(50)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetColor(color)  # Match the light color
    sphereActor.GetProperty().LightingOff()  # Disable lighting for this sphere

    renderer.AddActor(sphereActor)

def main():
    mainSphereActor = render_main_cone()

    renderer = vtkRenderer()
    renderer.SetBackground(0.2, 0.0, 0.4)
    renderer.AddActor(mainSphereActor)

    createLightWithSphere(renderer, (1, 0, 0), (-5, 0, 0))  # Red light
    createLightWithSphere(renderer, (0, 1, 0), (0, 0, -5))  # Green light
    createLightWithSphere(renderer, (0, 0, 1), (5, 0, 0))  # Blue light
    createLightWithSphere(renderer, (1, 1, 0), (0, 0, 5))  # Yellow light

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(700, 700)
    renderWindow.SetWindowName("Lights with Spheres")

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()