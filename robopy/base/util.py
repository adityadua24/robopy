def ctraj(T0, T1, N):
    from .common import ishomog
    from .quaternion import UnitQuaternion
    from .transforms import t2r
    from .transforms import transl
    assert type(N) is float or type(N) is int
    assert type(T0) is list or ishomog(T0, 4)
    assert type(T1) is list or ishomog(T1, 4)

    if type(T0) is list:
        for each in T0:
            assert ishomog(each, 4)
    if type(T1) is list:
        for each in T1:
            assert ishomog(each, 4)

    def one_to_one(T0, T1):
        rot_0 = t2r(T0)
        rot_1 = t2r(T1)
        transl_0 = T0[0:3, 3]
        transl_1 = T1[0:3, 3]
        q0 = UnitQuaternion.rot(rot_0)
        q1 = UnitQuaternion.rot(rot_1)
        rot_traj = []
        for i in range(1, N+1):
            rot_traj.append(q0.interp(q1, 1/N * i).to_rot())
        return 0

    if ishomog(T0, 4):
        if ishomog(T1, 4):
            return one_to_one(T0, T1)
        elif type(T1) is list:
            # one to many case
            pass
    elif type(T1) is list:
        if ishomog(T1, 4):
            # many to one case
            pass
        elif type(T1) is list:
            # Many to many case
            pass


def lspb():
    pass