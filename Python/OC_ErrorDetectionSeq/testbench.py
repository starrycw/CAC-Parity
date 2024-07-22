import CACParitySeq_DetectionEvaluation as CACParitySeq_DetectionEvaluation

SimuInstance_01 = CACParitySeq_DetectionEvaluation.DetectionEvaluation(bitwidth=7, n_dataTransCycle=32, instance_id=1)

SimuInstance_01.run_step1_createSimuTasks(tasks_idTuple=(0, 1),
                                          tasks_encoderTypeTuple=('FTF', 'XORParity'),
                                          tasks_errorGenType='bridgeDelayFaults_randomAdjacentBits',
                                          tasks_errorGenParam=(1, ))

SimuInstance_01.run_step2_startSimu(n_runCycle=10000,
                                    seqType='FTF',
                                    initialSeqType='all0')