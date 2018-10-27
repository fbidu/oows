import importlib


def test_exposed_modules():
    assert importlib.util.find_spec("oows"), "oows not found!"
    assert importlib.util.find_spec("oows.ecs"), "oows.ecs not found!"

    import oows

    assert hasattr(oows.ecs, "Cluster"), "ecs.Cluster not found!"
    assert hasattr(oows.ecs, "Service"), "ecs.Service not found!"
    assert hasattr(oows.ecs, "TaskDefinition"), "ecs.TaskDefinition not found!"
