from other.l04_linear_algebra.my_linear_algebra import Vector
import other.l04_linear_algebra.my_linear_algebra as mla



def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    assert len(v) == len(gradient)
    step = mla.scalar_multiply(step_size, gradient)
    return mla.add(v, step)
