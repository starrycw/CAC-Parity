# 20240720
import copy

########################################################################################################################
def FTFParity_EncoderCore(seq_c: tuple[int, ...], seq_d: tuple[int, ...]) -> tuple[int, ...]:
    '''
    Generate binary sequence G from binary sequences C and D.\n
    The input sequences C and D must have the same length.\n
    The elements in each sequence must be 0 or 1 (int).\n

    :param seq_c:
    :param seq_d:
    :return:
    '''
    assert isinstance(seq_c, tuple)
    assert isinstance(seq_d, tuple)
    seqLen = len(seq_c)
    assert len(seq_d) == seqLen

    # Step 1:
    seq_e_list = []
    for idx_i in range(0, seqLen):
        assert seq_c[idx_i] in (0, 1)
        assert seq_d[idx_i] in (0, 1)
        if idx_i % 2 == 0: # XOR
            if seq_c[idx_i] == seq_d[idx_i]:
                seq_e_list.append(0)
            else:
                seq_e_list.append(1)
        elif idx_i % 2 == 1: #XNOR
            if seq_c[idx_i] == seq_d[idx_i]:
                seq_e_list.append(1)
            else:
                seq_e_list.append(0)
        else:
            assert False
    seq_e = tuple(seq_e_list)

    # Step 2:
    for idx_i in range(0, seqLen):
        assert seq_e[idx_i] in (0, 1)
    seq_f_list = copy.deepcopy(seq_e_list)
    for idx_i in range(0, seqLen - 1):
        if idx_i % 2 == 0:
            if (seq_e[idx_i] == 0) and (seq_e[idx_i + 1] == 1):
                seq_f_list[idx_i] = copy.deepcopy(seq_c[idx_i])
                seq_f_list[idx_i + 1] = copy.deepcopy(seq_c[idx_i + 1])
    seq_f = tuple(seq_f_list)

    # Step 3:
    for idx_i in range(0, seqLen):
        assert seq_f[idx_i] in (0, 1)
    seq_g_list = copy.deepcopy(seq_f_list)
    for idx_i in range(1, seqLen - 1):
        if idx_i % 2 == 1:
            if (seq_f[idx_i] == 1) and (seq_f[idx_i + 1] == 0):
                seq_g_list[idx_i] = copy.deepcopy(seq_c[idx_i])
                seq_g_list[idx_i + 1] = copy.deepcopy(seq_c[idx_i + 1])
    seq_g = tuple(seq_g_list)

    for idx_i in range(0, seqLen):
        assert seq_g[idx_i] in (0, 1)

    return seq_g



########################################################################################################################
def FPFParity_EncoderCore(seq_c: tuple[int, ...], seq_d:tuple[int, ...]) -> tuple[int, ...]:
    '''
    Generate binary sequence G from binary sequences C and D.\n
    The input sequences C and D must have the same length.\n
    The elements in each sequence must be 0 or 1 (int).\n

    :param seq_c:
    :param seq_d:
    :return:
    '''
    assert isinstance(seq_c, tuple)
    assert isinstance(seq_d, tuple)
    seqLen = len(seq_c)
    assert len(seq_d) == seqLen

    # Step 1:
    seq_e_list = []
    for idx_i in range(0, seqLen):
        assert seq_c[idx_i] in (0, 1)
        assert seq_d[idx_i] in (0, 1)
        if idx_i % 2 == 0:  # XOR
            if seq_c[idx_i] == seq_d[idx_i]:
                seq_e_list.append(0)
            else:
                seq_e_list.append(1)
        elif idx_i % 2 == 1:  # XNOR
            if seq_c[idx_i] == seq_d[idx_i]:
                seq_e_list.append(1)
            else:
                seq_e_list.append(0)
        else:
            assert False
    seq_e = tuple(seq_e_list)

    # Step 2:
    for idx_i in range(0, seqLen):
        assert seq_e[idx_i] in (0, 1)
    seq_f_list = copy.deepcopy(seq_e_list)
    for idx_i in range(2, seqLen - 1):
        if idx_i % 2 == 0:
            if (seq_e[idx_i - 1], seq_e[idx_i], seq_e[idx_i + 1]) in ((1, 0, 1), (0, 1, 0)):
                seq_f_list[idx_i] = 1 - seq_f_list[idx_i]
    seq_f = tuple(seq_f_list)

    # Step 3:
    for idx_i in range(0, seqLen):
        assert seq_f[idx_i] in (0, 1)
    seq_g_list = copy.deepcopy(seq_f_list)
    for idx_i in range(1, seqLen - 1):
        if idx_i % 2 == 1:
            if (seq_f[idx_i - 1], seq_f[idx_i], seq_f[idx_i + 1]) in ((1, 0, 1), (0, 1, 0)):
                seq_g_list[idx_i] = 1 - seq_g_list[idx_i]
    seq_g = tuple(seq_g_list)

    for idx_i in range(0, seqLen):
        assert seq_g[idx_i] in (0, 1)

    return seq_g

########################################################################################################################
def XORParity_EncoderCore(seq_c: tuple[int, ...], seq_d:tuple[int, ...]) -> tuple[int, ...]:
    '''
    Generate binary sequence G from binary sequences C and D.\n
    The input sequences C and D must have the same length.\n
    The elements in each sequence must be 0 or 1 (int).\n

    :param seq_c:
    :param seq_d:
    :return:
    '''
    assert isinstance(seq_c, tuple)
    assert isinstance(seq_d, tuple)
    seqLen = len(seq_c)
    assert len(seq_d) == seqLen

    # Step 1:
    seq_e_list = []
    for idx_i in range(0, seqLen):
        assert seq_c[idx_i] in (0, 1)
        assert seq_d[idx_i] in (0, 1)
        if idx_i % 2 == 0:  # XOR
            if seq_c[idx_i] == seq_d[idx_i]:
                seq_e_list.append(0)
            else:
                seq_e_list.append(1)
        elif idx_i % 2 == 1:  # XOR
            if seq_c[idx_i] == seq_d[idx_i]:
                seq_e_list.append(0)
            else:
                seq_e_list.append(1)
        else:
            assert False
    seq_g = tuple(seq_e_list)
    return seq_g

###############################
###############################
# print(FTFParity_EncoderCore(seq_c=(1, 1, 1, 1, 1, 1), seq_d=(0, 0, 1, 1, 1, 0)))
#
# print(FTFParity_EncoderCore(seq_c=(1, 1, 1, 0, 1, 1), seq_d=(0, 0, 1, 1, 1, 0)))