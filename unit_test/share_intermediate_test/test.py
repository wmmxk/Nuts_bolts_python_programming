
from pytest_steps import test_steps


@test_steps('step_a', 'step_b', 'step_c')
def test_suite():
    # Step A
    print("step a")
    assert not False  # replace with your logic
    intermediate_a = 'hello'
    yield

    # Step B
    print("step b")
    assert True  # replace with your logic
    yield

    # Step C
    print("step c")
    new_text = intermediate_a + " ... augmented"
    print(new_text)
    assert len(new_text) == 19
    yield