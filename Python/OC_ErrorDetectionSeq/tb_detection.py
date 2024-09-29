import copy

import CACParitySeq_DetectionEvaluation as CACParitySeq_DetectionEvaluation

finalResult_list = []
finalResult_bestAndWorst_list = []

for simuparam_cycle_i in (8, 16, 32, 64):

    subtaskresult_list = [[0, 0], [0, 0], [0, 0]]
    best_case_list = [(10, 10, 0, None), (10, 10, 0, None)]
    worst_case_list = [(10, 0, 10, None), (10, 0, 10, None)]

    for errbit_idx_i in range(0, 16):

        SimuInstance_01 = CACParitySeq_DetectionEvaluation.DetectionEvaluation(bitwidth=16, n_dataTransCycle=simuparam_cycle_i)

        # ERROR:
        # ('sa0', sa1_idx_tuple)
        # ('sa1', sa1_idx_tuple)
        # ('delay01', delay_idx_tuple)
        # ('delay10', delay_idx_tuple)
        # ('bridgeStatic', bridge_idx_tuple)
        # ('bridgeDelay', bridge_idx_tuple)
        # ('NF_oneBitFlip', idx_cycle, idx_bit)

        SimuInstance_01.run_step1_createSimuTasks_specifyError(tasks_idTuple=(0, 1),
                                                               tasks_encoderTypeTuple=('FTF', 'XORParity'),
                                                               tasks_errorInjectorActive=('sa0', (errbit_idx_i, ))
                                                               )

        result_all, result_hidden, result_detected = SimuInstance_01.run_step2_startSimu(n_runCycle=1000000,
                                                                                         seqType='FTF',
                                                                                         initialSeqType='all0',
                                                                                         logsavelevel='no')

        for resultListIdx_i in (0, 1):
            if ((result_detected[resultListIdx_i] / result_all[resultListIdx_i]) > (best_case_list[resultListIdx_i][2] / best_case_list[resultListIdx_i][0])):
                best_case_list[resultListIdx_i] = (copy.deepcopy(result_all[resultListIdx_i]), copy.deepcopy(result_hidden[resultListIdx_i]), copy.deepcopy(result_detected[resultListIdx_i]), copy.deepcopy(errbit_idx_i))
            if ((result_detected[resultListIdx_i] / result_all[resultListIdx_i]) < (worst_case_list[resultListIdx_i][2] / worst_case_list[resultListIdx_i][0])):
                worst_case_list[resultListIdx_i] = (copy.deepcopy(result_all[resultListIdx_i]), copy.deepcopy(result_hidden[resultListIdx_i]), copy.deepcopy(result_detected[resultListIdx_i]), copy.deepcopy(errbit_idx_i))

        for resultListIdx_i in (0, 1):
            subtaskresult_list[0][resultListIdx_i] = subtaskresult_list[0][resultListIdx_i] + result_all[resultListIdx_i]
            subtaskresult_list[1][resultListIdx_i] = subtaskresult_list[1][resultListIdx_i] + result_hidden[resultListIdx_i]
            subtaskresult_list[2][resultListIdx_i] = subtaskresult_list[2][resultListIdx_i] + result_detected[resultListIdx_i]

        subtaskresult_tuple = tuple(subtaskresult_list)

    finalResult_list.append((copy.deepcopy(simuparam_cycle_i),
                             copy.deepcopy(subtaskresult_tuple)))

    finalResult_bestAndWorst_list.append((copy.deepcopy(simuparam_cycle_i),
                                         copy.deepcopy(best_case_list),
                                         copy.deepcopy(worst_case_list)))

print("Final Result: \n {}".format(finalResult_list))
print("Best and Worst Case: \n {}".format(finalResult_bestAndWorst_list))