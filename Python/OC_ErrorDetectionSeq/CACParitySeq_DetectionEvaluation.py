# 20240721
import datetime
import copy
import random

import CACParitySeq_EncoderTop as CACParitySeq_EncoderTop



class DetectionEvaluation:
    def __init__(self, bitwidth, n_dataTransCycle, instance_id = None):
        self._instance_id = copy.deepcopy(instance_id)
        assert isinstance(bitwidth, int)
        assert bitwidth > 3
        self._param_bitwidth = copy.deepcopy(bitwidth) # 数据位宽
        assert isinstance(n_dataTransCycle, int)
        assert n_dataTransCycle > 3
        self._param_nDataTransCycle = copy.deepcopy(n_dataTransCycle) # 数据连续传输的周期
        self._taskList_id = [] # 任务id
        self._taskList_encoder = [] # 编码器instance
        self._task_errorInjectorType = None # 故障注入配置，经generateErrorInjectorConfig处理后才能获得实际生效的故障注入配置
        self._task_errorInjectorActive = None # 实际生效的故障注入配置




    def getParam_numberOfTasks(self):
        return len(self._taskList_encoder)

    def getParam_taskInfo_id(self, task_idx):
        return copy.deepcopy(self._taskList_id[task_idx])

    def getParam_taskInfo_encoder(self, task_idx):
        return copy.deepcopy(self._taskList_encoder[task_idx])

    def getParam_bitwidth(self):
        '''
        返回seq位宽
        :return:
        '''
        return copy.deepcopy(self._param_bitwidth)

    def getParam_nDataTransCycle(self):
        '''
        返回数据连续传输的周期
        :return:
        '''
        return copy.deepcopy(self._param_nDataTransCycle)

    def generateErrorInjectorConfig(self, errorGenType, errorGenParam:tuple[int, ...]):
        '''
        用于生成关于如何向序列中添加错误的配置。\n
        -------\n
        errorGenType - errorGenParam ：解释\n
        'SA0_randomBits' - (n_SA0(int), ) : 为随机的n_SA0个数据线添加SA0故障。\n
        'SA1_randomBits' - (n_SA1(int), ) : 为随机的n_SA1个数据线添加SA1故障。\n
        'xtalkDelay_randomBits' - (n_bits(int), xtalk_threshold(int))：为随机的n_bits个数据线添加xtalk引起的延迟故障。假设当相邻两位对其的串扰级别超过xtalk_threshold时，会引发错误。\n
        'delay_01_randomBits' - (n_bits(int), )：为随机的n_bits个数据线添加0->1跳变时间过长的延迟故障。\n
        'delay_10_randomBits' - (n_bits(int), )：为随机的n_bits个数据线添加1->0跳变时间过长的延迟故障。\n
        'bridgeStaticFaults_randomAdjacentBits' - (n_pairs(int), )：为随机的n_pairs对相邻线添加bridge static fault（详见./FaultModel/bridge_static.png）。其中，aggressor和victim随机选择。\n
        'bridgeDelayFaults_randomAdjacentBits' - (n_pairs(int), )：为随机的n_pairs对相邻线添加bridge delay fault（详见./FaultModel/bridge_delay.png）。其中，aggressor和victim随机选择。\n
        'NotFault_oneBitFlip' - (idx_cycle(int), idx_bit(int))：翻转第idx_cycle个传输周期中索引为idx_bit的比特。\n
        -------\n

        :param errorGenType:所生成错误的类型\n
        :param errorGenParam:错误生成所需的配置变量\n
        :return:
        '''

        if errorGenType == 'SA0_randomBits':
            assert len(errorGenParam) == 1
            assert self.getParam_bitwidth() >= errorGenParam[0]
            sa0_idx_list = []
            sa0_idx_candidate = list(range(0, self.getParam_bitwidth()))
            while len(sa0_idx_list) < errorGenParam[0]:
                sa0_idx_selected = random.choice(sa0_idx_candidate)
                sa0_idx_list.append(copy.deepcopy(sa0_idx_selected))
                sa0_idx_candidate.remove(sa0_idx_selected)
            sa0_idx_tuple = tuple(copy.deepcopy(sa0_idx_list))
            return ('sa0', sa0_idx_tuple)

        elif errorGenType == 'SA1_randomBits':
            assert len(errorGenParam) == 1
            assert self.getParam_bitwidth() >= errorGenParam[0]
            sa1_idx_list = []
            sa1_idx_candidate = list(range(0, self.getParam_bitwidth()))
            while len(sa1_idx_list) < errorGenParam[0]:
                sa1_idx_selected = random.choice(sa1_idx_candidate)
                sa1_idx_list.append(copy.deepcopy(sa1_idx_selected))
                sa1_idx_candidate.remove(sa1_idx_selected)
            sa1_idx_tuple = tuple(copy.deepcopy(sa1_idx_list))
            return ('sa1', sa1_idx_tuple)

        # elif errorGenType == 'xtalkDelay_randomBits':
        #     assert len(errorGenParam) == 2
        #     assert self.getParam_bitwidth() >= errorGenParam[0]
        #     xtalkDelay_idx_list = []
        #     xtalkDelay_idx_candidate = list(range(0, self.getParam_bitwidth()))
        #     while len(xtalkDelay_idx_list) < errorGenParam[0]:
        #         xtalkDelay_idx_selected = random.choice(xtalkDelay_idx_candidate)
        #         xtalkDelay_idx_list.append(copy.deepcopy(xtalkDelay_idx_selected))
        #         xtalkDelay_idx_candidate.remove(xtalkDelay_idx_selected)
        #     xtalkDelay_idx_tuple = tuple(copy.deepcopy(xtalkDelay_idx_list))
        #     return ('xtalkDelay', xtalkDelay_idx_tuple, copy.deepcopy(errorGenParam[1]))

        elif errorGenType == 'delay_01_randomBits':
            assert len(errorGenParam) == 1
            assert self.getParam_bitwidth() >= errorGenParam[0]
            delay_idx_list = []
            delay_idx_candidate = list(range(0, self.getParam_bitwidth()))
            while len(delay_idx_list) < errorGenParam[0]:
                delay_idx_selected = random.choice(delay_idx_candidate)
                delay_idx_list.append(copy.deepcopy(delay_idx_selected))
                delay_idx_candidate.remove(delay_idx_selected)
            delay_idx_tuple = tuple(copy.deepcopy(delay_idx_list))
            return ('delay01', delay_idx_tuple)

        elif errorGenType == 'delay_10_randomBits':
            assert len(errorGenParam) == 1
            assert self.getParam_bitwidth() >= errorGenParam[0]
            delay_idx_list = []
            delay_idx_candidate = list(range(0, self.getParam_bitwidth()))
            while len(delay_idx_list) < errorGenParam[0]:
                delay_idx_selected = random.choice(delay_idx_candidate)
                delay_idx_list.append(copy.deepcopy(delay_idx_selected))
                delay_idx_candidate.remove(delay_idx_selected)
            delay_idx_tuple = tuple(copy.deepcopy(delay_idx_list))
            return ('delay10', delay_idx_tuple)

        elif errorGenType == 'bridgeStaticFaults_randomAdjacentBits':
            assert len(errorGenParam) == 1
            assert self.getParam_bitwidth() >= (errorGenParam[0] * 2)
            bridge_idx_list = []
            bridge_idx_candidate = list(range(0, (self.getParam_bitwidth() - 1)))
            while len(bridge_idx_list) < errorGenParam[0]:
                bridge_idx_selected = random.choice(bridge_idx_candidate)
                genOrder_random = random.choice((False, True))
                if genOrder_random is False:
                    bridge_idx_list.append(
                        (copy.deepcopy(bridge_idx_selected), (copy.deepcopy(bridge_idx_selected) + 1)))
                elif genOrder_random is True:
                    bridge_idx_list.append(
                        ((copy.deepcopy(bridge_idx_selected) + 1), copy.deepcopy(bridge_idx_selected)))
                else:
                    assert False
                bridge_idx_candidate.remove(bridge_idx_selected)
                bridge_idx_candidate.remove(bridge_idx_selected + 1)
            bridge_idx_tuple = tuple(copy.deepcopy(bridge_idx_list))
            return ('bridgeStatic', bridge_idx_tuple)

        elif errorGenType == 'bridgeDelayFaults_randomAdjacentBits':
            assert len(errorGenParam) == 1
            assert self.getParam_bitwidth() >= (errorGenParam[0] * 2)
            bridge_idx_list = []
            bridge_idx_candidate = list(range(0, (self.getParam_bitwidth() - 1)))
            while len(bridge_idx_list) < errorGenParam[0]:
                bridge_idx_selected = random.choice(bridge_idx_candidate)
                genOrder_random = random.choice((False, True))
                if genOrder_random is False:
                    bridge_idx_list.append(
                        (copy.deepcopy(bridge_idx_selected), (copy.deepcopy(bridge_idx_selected) + 1)))
                elif genOrder_random is True:
                    bridge_idx_list.append(
                        ((copy.deepcopy(bridge_idx_selected) + 1), copy.deepcopy(bridge_idx_selected)))
                else:
                    assert False
                bridge_idx_candidate.remove(bridge_idx_selected)
                bridge_idx_candidate.remove(bridge_idx_selected + 1)
            bridge_idx_tuple = tuple(copy.deepcopy(bridge_idx_list))
            return ('bridgeDelay', bridge_idx_tuple)

        elif errorGenType == 'NotFault_oneBitFlip':
            assert len(errorGenParam) == 2
            assert self.getParam_bitwidth() > errorGenParam[1]
            assert errorGenParam[1] >= 0
            assert self.getParam_nDataTransCycle() >= errorGenParam[0]
            assert errorGenParam[0] > 0
            return ('NF_oneBitFlip', copy.deepcopy(errorGenParam[0], copy.deepcopy(errorGenParam[1])))

        else:
            assert False

    def getParam_errorInjectorActive(self):
        return copy.deepcopy(self._task_errorInjectorActive)

    def getParam_errorInjectorType(self):
        return copy.deepcopy(self._task_errorInjectorType)

    def run_step1_createSimuTasks(self, tasks_idTuple, tasks_encoderTypeTuple, tasks_errorGenType, tasks_errorGenParam):
        '''
        添加仿真任务。
        tasks_idTuple, tasks_encoderTypeTuple应当为2个元素数目相同的元组。三个元组中同一idx的元素之间是关联的。\n
        其中:\n
        tasks_idTuple中为任务的id。\n
        tasks_encoderTypeTuple中为任务的编码器类型，例如'FPF','FTF','XORParity'。\n
        tasks_errorGenType和tasks_errorGenParam指定了故障类型，详见generateErrorInjectorConfig方法的注释。\n

        需要注意的是，在该仿真中，所有任务具有相同的位宽、源数据、故障、数据连续传输周期；它们彼此不同的是编码器类型。\n
        此外，本方法不检查tasks_idTuple, tasks_encoderTypeTuple, tasks_errorType是否有错误！如果存在错误，可能到仿真运行阶段才会报错！
        :param tasks_idTuple:
        :param tasks_encoderTypeTuple:
        :param tasks_errorGenType:
        :param tasks_errorGenParam:
        :return:
        '''
        assert isinstance(tasks_idTuple, tuple)
        assert isinstance(tasks_encoderTypeTuple, tuple)
        assert len(tasks_idTuple) == len(tasks_encoderTypeTuple)
        self._taskList_id = copy.deepcopy(tasks_idTuple)
        self._taskList_encoder = copy.deepcopy(tasks_encoderTypeTuple)
        # for idx_j in range(0, len(tasks_encoderTypeTuple)):
        #     self._taskSimuState_seqTransmitted_lastCycle.append(self.getParam_bitwidth() * [0])
        self._task_errorInjectorType = (copy.deepcopy(tasks_errorGenType), copy.deepcopy(tasks_errorGenParam))


        # Get self._task_errorInjectorActive
        self._task_errorInjectorActive = self.generateErrorInjectorConfig(errorGenType=copy.deepcopy(tasks_errorGenType),
                                                                          errorGenParam=copy.deepcopy(tasks_errorGenParam))
        print('[DetectionEval] - Step1 OK!')
        print('---  ID: {}'.format(tasks_idTuple))
        print('--- ENC: {}'.format(tasks_encoderTypeTuple))
        print('--- ERR-TYPE: {}'.format(self.getParam_errorInjectorType()))
        print('--- ERR-ACTIVE: {}'.format(self.getParam_errorInjectorActive()))
        print('---------------')

    def _substep_genSourceSeq_random(self, seqType):
        '''
        随机生成符合FTF/FPF约束的序列。

        :param seqType: in ('FTF', 'FPF')
        :return:
        '''
        if seqType == 'FTF':
            seqGen_list = []
            for idx_i in range(0, self.getParam_bitwidth()):
                bitGen_random = random.choice((0, 1))
                if idx_i > 0:
                    if (idx_i % 2 == 1) and (seqGen_list[-1] == 0):
                        bitGen_random = 0
                    if (idx_i % 2 == 0) and (seqGen_list[-1] == 1):
                        bitGen_random = 1
                seqGen_list.append(copy.deepcopy(bitGen_random))
            seqGen = tuple(copy.deepcopy(seqGen_list))
            return seqGen
        elif seqType == 'FPF':
            seqGen_list = []
            for idx_i in range(0, self.getParam_bitwidth()):
                bitGen_random = random.choice((0, 1))
                if idx_i > 1:
                    if seqGen_list[-1] != seqGen_list[-2]:
                        bitGen_random = copy.deepcopy(seqGen_list[-1])
                seqGen_list.append(copy.deepcopy(bitGen_random))
            seqGen = tuple(copy.deepcopy(seqGen_list))
            return seqGen

    def _substep_seqErrorInjection(self, seq_tuple, cycleIdx_seq, seq_lastCycle):
        '''
        向序列seq_tuple中注入错误。\n
        cycleIdx_seq是当前seq_tuple的周期数，从1开始，当error类型为‘NF_oneBitFlip’时，需要通过该变量来翻转比特。
        seq_lastCycle是上一周期末态的seq
        :param seq_tuple:
        :param cycleIdx_seq:
        :param seq_lastCycle:
        :return:
        '''
        assert isinstance(seq_tuple, tuple)
        assert len(seq_tuple) == self.getParam_bitwidth()
        assert cycleIdx_seq > 0
        assert cycleIdx_seq <= self.getParam_nDataTransCycle() + 1
        eia_info = self.getParam_errorInjectorActive() # eia - Error Injector Active
        seq_list = list(seq_tuple)

        if eia_info[0] == 'sa0': # ('sa0', sa0_idx_tuple)
            for errorIdx_i in eia_info[1]:
                seq_list[errorIdx_i] = 0

        elif eia_info[0] == 'sa1': #
            for errorIdx_i in eia_info[1]:
                seq_list[errorIdx_i] = 1

        elif eia_info[0] == 'delay01': # ('delay01', delay_idx_tuple)
            for errorIdx_i in eia_info[1]:
                if seq_lastCycle[errorIdx_i] == 0:
                    seq_list[errorIdx_i] = 0

        elif eia_info[0] == 'delay10': # ('delay10', delay_idx_tuple)
            for errorIdx_i in eia_info[1]:
                if seq_lastCycle[errorIdx_i] == 1:
                    seq_list[errorIdx_i] = 1

        elif eia_info[0] == 'bridgeStatic': # ('bridgeStatic', bridge_idx_tuple)
            for errorIdxPair_i in eia_info[1]:
                seq_list[errorIdxPair_i[1]] = copy.deepcopy(seq_tuple[errorIdxPair_i[0]])

        elif eia_info[0] == 'bridgeDelay': # ('bridgeDelay', bridge_idx_tuple)
            for errorIdxPair_i in eia_info[1]:
                if ((seq_lastCycle[errorIdxPair_i[0]] == seq_tuple[errorIdxPair_i[0]]) and
                        (seq_lastCycle[errorIdxPair_i[0]] == seq_lastCycle[errorIdxPair_i[1]]) and
                        (seq_lastCycle[errorIdxPair_i[0]] != seq_tuple[errorIdxPair_i[1]])):
                    seq_list[errorIdxPair_i[1]] = copy.deepcopy(seq_tuple[errorIdxPair_i[0]])
                elif ((seq_lastCycle[errorIdxPair_i[1]] == seq_tuple[errorIdxPair_i[1]]) and
                        (seq_lastCycle[errorIdxPair_i[1]] == seq_lastCycle[errorIdxPair_i[0]]) and
                        (seq_lastCycle[errorIdxPair_i[1]] != seq_tuple[errorIdxPair_i[0]])):
                    seq_list[errorIdxPair_i[0]] = copy.deepcopy(seq_tuple[errorIdxPair_i[1]])
        elif eia_info[0] == 'NF_oneBitFlip':
            if eia_info[1] == cycleIdx_seq:
                seq_list[eia_info[2]] = 1 - seq_list[eia_info[2]]

        else:
            assert False

        seqWithError_tuple = tuple(seq_list)

        return seqWithError_tuple


    def run_step2_startSimu(self, n_runCycle, seqType, initialSeqType):
        assert initialSeqType in ('all0', 'theLastParitySeq')
        assert isinstance(n_runCycle, int)
        assert n_runCycle > 0


        # Export to files
        note_timestring = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        logFile =  open("exported_files/DetectionEval_{}_{}.log".format(note_timestring, random.random()), 'x')

        # Initialize vars
        taskList_seqTransmittedNow = []
        for idx_i in range(0, self.getParam_numberOfTasks()):
            taskList_seqTransmittedNow.append(self.getParam_bitwidth() * (0, ))
        taskListGolden_seqTransmittedNow = []
        for idx_i in range(0, self.getParam_numberOfTasks()):
            taskListGolden_seqTransmittedNow.append(self.getParam_bitwidth() * (0, ))

        # Initialize encoders
        encoderInstance_list = []
        encoderInstanceGolden_list = []
        for idx_i in range(0, self.getParam_numberOfTasks()):
            encoderInstance_list.append(CACParitySeq_EncoderTop.CACParitySeqEncoderTop(CACName=self.getParam_taskInfo_encoder(task_idx=idx_i),
                                                                                       n_seq=self.getParam_bitwidth(),
                                                                                       nDataTransCycle=self.getParam_nDataTransCycle()))
            encoderInstanceGolden_list.append(CACParitySeq_EncoderTop.CACParitySeqEncoderTop(CACName=self.getParam_taskInfo_encoder(task_idx=idx_i),
                                                                                             n_seq=self.getParam_bitwidth(),
                                                                                             nDataTransCycle=self.getParam_nDataTransCycle()))


        # Monitor & Statistics
        cnt_taskList_caseAll = self.getParam_numberOfTasks() * [0]
        cnt_taskList_caseDetected = self.getParam_numberOfTasks() * [0]
        cnt_taskList_caseHidden = self.getParam_numberOfTasks() * [0]


        # Start!
        logFile.write('CACParitySeq_DetectionEvaluation\n')
        logFile.write('---------------------------------\n')
        logFile.write('Simulation Info:\n')
        logFile.write('--- Timestamp: {}')
        logFile.write('--- Number of tasks: {}\n'.format(self.getParam_numberOfTasks()))
        logFile.write('--- Bitwidth: {}\n'.format(self.getParam_bitwidth()))
        logFile.write('--- Data trans cycle: {}\n'.format(self.getParam_nDataTransCycle()))
        logFile.write('--- Fault injector active: {}\n'.format(self.getParam_errorInjectorActive()))
        logFile.write('--- Seq type: {}\n'.format(seqType))
        logFile.write('--- InitialSeqType: {}\n'.format(initialSeqType))
        logFile.write('--- Task details:\n')
        for idx_i in range(0, self.getParam_numberOfTasks()):
            logFile.write('--- Task {}: ID={}, Encoder={}\n'.format(idx_i, self.getParam_taskInfo_id(task_idx=idx_i), self.getParam_taskInfo_encoder(task_idx=idx_i)))
        logFile.flush() #刷新缓冲区
        for simuCycle_i in range(0, n_runCycle):
            logFile.write('---------------------------------\n')
            logFile.write('# SimulationRound-{}\n'.format(simuCycle_i))

            # 非Parity数据传输周期
            for dataTransCycle_i in range(1, self.getParam_nDataTransCycle() + 1):
                # 生成原始数据
                seqNoError = self._substep_genSourceSeq_random(seqType=seqType)
                logFile.write('- Cycle{} - Seq generated: {}\n'.format(dataTransCycle_i, seqNoError))

                # # 数据传输 - 无故障对照
                # if dataTransCycle_i == 1:
                #     encoderInstance_golden.run_transmit_firstCycle(seq2bTrans=copy.deepcopy(seqNoError))
                # elif (dataTransCycle_i > 1) and (dataTransCycle_i <= self.getParam_nDataTransCycle()):
                #     encoderInstance_golden.run_transmit_notFirstCycle(seq2bTrans=copy.deepcopy(seqNoError))
                # else:
                #     assert False
                #
                # taskGolden_seqTransmittedNow = copy.deepcopy(seqNoError)

                # 数据传输 - tasks
                for taskIdx_ii in range(0, self.getParam_numberOfTasks()):
                    seqWithError = self._substep_seqErrorInjection(seq_tuple=seqNoError,
                                                                   cycleIdx_seq=dataTransCycle_i,
                                                                   seq_lastCycle=copy.deepcopy(taskList_seqTransmittedNow[taskIdx_ii]))

                    if dataTransCycle_i == 1:
                        encoderInstance_list[taskIdx_ii].run_transmit_firstCycle(seq2bTrans=copy.deepcopy(seqWithError))
                        encoderInstanceGolden_list[taskIdx_ii].run_transmit_firstCycle(seq2bTrans=copy.deepcopy(seqNoError))
                    elif (dataTransCycle_i > 1) and (dataTransCycle_i <= self.getParam_nDataTransCycle()):
                        encoderInstance_list[taskIdx_ii].run_transmit_notFirstCycle(seq2bTrans=copy.deepcopy(seqWithError))
                        encoderInstanceGolden_list[taskIdx_ii].run_transmit_notFirstCycle(seq2bTrans=copy.deepcopy(seqNoError))
                    else:
                        assert False

                    # 更新总线上的数据
                    taskListGolden_seqTransmittedNow[taskIdx_ii] = copy.deepcopy(seqNoError)
                    if self.getParam_errorInjectorActive()[0] in ('sa0', 'sa1', 'bridgeStatic'):
                        taskList_seqTransmittedNow[taskIdx_ii] = copy.deepcopy(seqWithError)
                    elif self.getParam_errorInjectorActive()[0] in ('delay01', 'delay10', 'bridgeDelay', 'NF_oneBitFlip'):
                        taskList_seqTransmittedNow[taskIdx_ii] = copy.deepcopy(seqNoError)
                    else:
                        assert False

            # Parity数据传输周期 - tasks - 接收端计算出的Parity序列
            paritySeqsList_sinkGen = []
            for taskIdx_ii in range(0, self.getParam_numberOfTasks()):
                paritySeqsList_sinkGen.append(copy.deepcopy(encoderInstance_list[taskIdx_ii].run_readOutParitySeq()))

            # Parity数据传输周期 - tasks - 实际收到的Parity序列
            paritySeqsList_sinkRec_noError = []
            paritySeqsList_sinkRec_withError = []
            for taskIdx_ii in range(0, self.getParam_numberOfTasks()):
                paritySeqsSinkRec =  encoderInstanceGolden_list[taskIdx_ii].run_readOutParitySeq()
                paritySeqsList_sinkRec_noError.append(copy.deepcopy(paritySeqsSinkRec))
                paritySeqsList_sinkRec_withError.append(copy.deepcopy(self._substep_seqErrorInjection(seq_tuple=paritySeqsSinkRec,
                                                                                                      cycleIdx_seq=(self.getParam_nDataTransCycle() + 1),
                                                                                                      seq_lastCycle=taskList_seqTransmittedNow[taskIdx_ii])))

            # 准备下一轮仿真的初态
            for taskIdx_ii in range(0, self.getParam_numberOfTasks()):
                if initialSeqType == 'theLastParitySeq':
                    taskListGolden_seqTransmittedNow[taskIdx_ii] = copy.deepcopy(paritySeqsList_sinkRec_noError[taskIdx_ii])
                    if self.getParam_errorInjectorActive()[0] in ('sa0', 'sa1', 'bridgeStatic'):
                        taskList_seqTransmittedNow[taskIdx_ii] = copy.deepcopy(paritySeqsList_sinkRec_withError[taskIdx_ii])
                    elif self.getParam_errorInjectorActive()[1] in ('delay01', 'delay10', 'bridgeDelay', 'NF_oneBitFlip'):
                        taskList_seqTransmittedNow[taskIdx_ii] = copy.deepcopy(paritySeqsList_sinkRec_noError[taskIdx_ii])
                    else:
                        assert False
                elif initialSeqType == 'all0':
                    taskListGolden_seqTransmittedNow[taskIdx_ii] = self.getParam_bitwidth() * (0, )
                    taskList_seqTransmittedNow[taskIdx_ii] = self.getParam_bitwidth() * (0, )

            # 比较
            for taskIdx_ii in range(0, self.getParam_numberOfTasks()):
                cnt_taskList_caseAll[taskIdx_ii] = cnt_taskList_caseAll[taskIdx_ii] + 1
                if paritySeqsList_sinkGen[taskIdx_ii] == paritySeqsList_sinkRec_withError[taskIdx_ii]:
                    cnt_taskList_caseHidden[taskIdx_ii] = cnt_taskList_caseHidden[taskIdx_ii] + 1
                    logFile.write('- task {} - HIDDEN: SinkGen_{} = SinkRec_{}\n'.format(taskIdx_ii, paritySeqsList_sinkGen[taskIdx_ii], paritySeqsList_sinkRec_withError[taskIdx_ii]))
                elif paritySeqsList_sinkGen[taskIdx_ii] != paritySeqsList_sinkRec_withError[taskIdx_ii]:
                    cnt_taskList_caseDetected[taskIdx_ii] = cnt_taskList_caseDetected[taskIdx_ii] + 1
                    logFile.write('- task {} - DETECTED: SinkGen_{} = SinkRec_{}\n'.format(taskIdx_ii, paritySeqsList_sinkGen[taskIdx_ii], paritySeqsList_sinkRec_withError[taskIdx_ii]))
                else:
                    assert False
            print('SimulationRound {} Finished! Current Data:'.format(simuCycle_i))
            print('--- Case ALL: {}, Case Hidden: {}, Case Detected: {}.\n'.format(cnt_taskList_caseAll,
                                                                                         cnt_taskList_caseHidden,
                                                                                         cnt_taskList_caseDetected))
            logFile.write('SimulationRound {} Finished! Current Data:\n'.format(simuCycle_i))
            logFile.write('--- Case ALL: {}, Case Hidden: {}, Case Detected: {}.\n'.format(cnt_taskList_caseAll,
                                                                                         cnt_taskList_caseHidden,
                                                                                         cnt_taskList_caseDetected))
        logFile.close()















