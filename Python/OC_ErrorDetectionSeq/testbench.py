import CACParitySeq_DetectionEvaluation as CACParitySeq_DetectionEvaluation

SimuInstance_01 = CACParitySeq_DetectionEvaluation.DetectionEvaluation(bitwidth=16, n_dataTransCycle=16, instance_id=1)

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
                                                       tasks_errorInjectorActive=('sa0', (3, ))
                                                       )

SimuInstance_01.run_step2_startSimu(n_runCycle=100,
                                    seqType='FTF',
                                    initialSeqType='all0',
                                    logsavelevel='mini')