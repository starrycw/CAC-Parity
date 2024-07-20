# 20240720
import CACParitySeq_EncoderCore as CACParitySeq_EncoderCore
import copy


class CACParitySeqEncoderTop:
    def __init__(self, CACName, n_seq, nDataTransCycle):
        '''

        :param CACName:
        :param n_seq: 序列位宽
        :param nDataTransCycle: 数据传输周期。即：传输这么多周期的数据后生成校验序列。
        '''
        assert CACName in ('FTF', 'FPF')
        assert isinstance(n_seq, int)
        assert n_seq > 3

        # Configurations
        self._param_CACName = copy.deepcopy(CACName) # CAC类型名称
        self._param_seqLength = copy.deepcopy(n_seq) # 序列位宽
        self._param_nDataTransCycle = copy.deepcopy(nDataTransCycle) # 数据传输周期。即：传输这么多周期的数据后生成校验序列。

        # Vars for simulation
        self._state_currentState = 'reset' # 当前状态
        # self._param_nDataCycle = None # 数据传输周期。即：传输这么多周期的数据后生成校验序列。
        self._state_currentCycle = 0 # 当前的数据传输周期（1 ~ self._param_nDataTransCycle），仅在reset状态为0。
        self._state_currentParitySeq = None # 当前的校验序列。

    def _currentState_get(self):
        '''
        获取当前状态
        :return:
        '''
        return copy.deepcopy(self._state_currentState)

    def _currentCycle_get(self):
        '''
        获取当前数据传输周期(1~N)
        :return:
        '''
        return copy.deepcopy(self._state_currentCycle)

    def _currentCycle_plusOne(self):
        '''
        当前传输周期加一
        :return:
        '''
        self._state_currentCycle = self._state_currentCycle + 1

    def _currentParitySeq_get(self):
        '''
        获取当前Parity序列
        :return:
        '''
        return copy.deepcopy(self._state_currentParitySeq)

    def _getParam_nDataTransCycle(self):
        '''
        获取设置的数据传输周期。即：传输这么多周期的数据后生成校验序列。
        :return:
        '''
        return copy.deepcopy(self._param_nDataTransCycle)

    def _getParam_seqLength(self):
        '''
        获取设置的序列位宽。
        :return:
        '''
        return copy.deepcopy(self._param_seqLength)

    def _getParam_CACName(self):
        '''
        获取设置的CAC名称。
        :return:
        '''
        return copy.deepcopy(self._param_CACName)

    def _resetTransmission(self):
        '''
        重置传输相关的变量。
        :return:
        '''
        self._state_currentCycle = 0
        self._state_currentParitySeq = None
    def _currentState_forceSet(self, newState):
        '''
        [慎用！] 强制更改当前状态。
        一般情况下，请使用self._changeState_event_xxx来修改状态！
        :param newState:
        :return:
        '''
        assert newState in ('reset', 'transmission', 'output')
        print("[Warning] The working state is forcibly changed from {} to {}!".format(self._currentState_get(), newState))
        self._state_currentState = copy.deepcopy(newState)
        if newState == 'reset':
            self._resetTransmission()


    def _changeState_event_newTransmissionStart(self):
        '''
        将要开始新传输时执行该方法。由reset状态进入transmission状态。
        :return:
        '''
        assert self._currentState_get() == 'reset'
        assert self._currentCycle_get() == 0
        assert self._currentParitySeq_get() is None
        self._state_currentState = 'transmission'

    def _changeState_event_transmissionFinished(self):
        '''
        传输结束时(即最终的parity序列已更新时)执行该方法，表明已经准备好读出parity序列了，由transmission状态进入output状态。
        :return:
        '''
        assert self._currentState_get() == 'transmission'
        assert self._currentCycle_get() == self._getParam_nDataTransCycle()
        self._state_currentState = 'output'

    def _changeState_event_parityHasBeenReadOut(self):
        '''
        Parity已经被读出后执行该方法，由output状态进入reset状态。
        :return:
        '''
        assert self._currentState_get() == 'output'
        assert self._currentCycle_get() == self._getParam_nDataTransCycle()
        self._state_currentState = 'reset'
        self._resetTransmission()

    def _updateCurrentParitySeq(self, newSeq):
        '''
        修改当前parity序列。
        注意：此方法不检查输入的newSeq！
        :param newSeq:
        :return:
        '''
        self._state_currentParitySeq = copy.deepcopy(newSeq)

    def run_transmit_firstCycle(self, seq2bTrans: tuple[int, ...]):
        '''
        传输第一个周期
        :param seq2bTrans:
        :return:
        '''
        assert self._currentState_get() == 'reset'
        assert isinstance(seq2bTrans, tuple)
        assert len(seq2bTrans) == self._getParam_seqLength()
        for idx_i in range(0, self._getParam_seqLength()):
            assert seq2bTrans[idx_i] in (0, 1)
        self._changeState_event_newTransmissionStart()
        self._updateCurrentParitySeq(newSeq=copy.deepcopy(seq2bTrans))
        assert self._currentCycle_get() == 0
        self._currentCycle_plusOne()

    def run_transmit_notFirstCycle(self, seq2bTrans: tuple[int, ...]):
        '''
        传输一个周期（非第一个周期）。
        :param seq2bTrans:
        :return:
        '''
        assert self._currentState_get() == 'transmission'
        assert isinstance(seq2bTrans, tuple)
        assert len(seq2bTrans) == self._getParam_seqLength()

        if self._getParam_CACName() == 'FTF':
            newParitySeq_tuple = CACParitySeq_EncoderCore.FTFParity_EncoderCore(seq_c=self._currentParitySeq_get(),
                                                                                seq_d=copy.deepcopy(seq2bTrans))
        elif self._getParam_CACName() == 'FPF':
            newParitySeq_tuple = CACParitySeq_EncoderCore.FPFParity_EncoderCore(seq_c=self._currentParitySeq_get(),
                                                                                seq_d=copy.deepcopy(seq2bTrans))
        else:
            assert False

        self._updateCurrentParitySeq(newSeq=copy.deepcopy(newParitySeq_tuple))
        assert self._currentCycle_get() > 0
        assert self._currentCycle_get() < self._getParam_nDataTransCycle()
        self._currentCycle_plusOne()

        if self._currentCycle_get() == self._getParam_nDataTransCycle():
            self._changeState_event_transmissionFinished()

    def run_readOutParitySeq(self):
        '''
        返回最终的Parity序列。
        注意，执行此方法时将自动reset！因此无法重复执行！
        :return:
        '''
        assert self._currentState_get() == 'output'
        paritySeqGenerated = copy.deepcopy(self._currentParitySeq_get())
        self._changeState_event_parityHasBeenReadOut()
        return paritySeqGenerated




