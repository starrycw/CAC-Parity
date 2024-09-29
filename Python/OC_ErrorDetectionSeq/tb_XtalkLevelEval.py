import XtalkLevelEvaluation as XtalkLevelEvaluation

######################################################
# n_checkPeriod = 100
# n_dataCycle = 8
#
# simu_instance = XtalkLevelEvaluation.XtalkLevelEval()
# cntInstance_FTF, cntInstance_XOR, cntInstance_noParity, cntInstance_PPC = simu_instance.runSimu_16x16Array_FTF(n_dataCycle=n_dataCycle,
#                                                                                                                n_simuPeriod=n_checkPeriod)
#
# xtalkCnt_FTF_rec_dict = cntInstance_FTF.get_cnt_rec()
# xtalkCnt_FTF_hex_dict = cntInstance_FTF.get_cnt_hex()
# xtalkCnt_XOR_rec_dict = cntInstance_XOR.get_cnt_rec()
# xtalkCnt_XOR_hex_dict = cntInstance_XOR.get_cnt_hex()
# xtalkCnt_noParity_rec_dict = cntInstance_noParity.get_cnt_rec()
# xtalkCnt_noParity_hex_dict = cntInstance_noParity.get_cnt_hex()
# xtalkCnt_PPC_rec_dict = cntInstance_PPC.get_cnt_rec()
# xtalkCnt_PPC_hex_dict = cntInstance_PPC.get_cnt_hex()
#
# print("RecArray:")
# print("xtalk - cnt_FTFParity - cnt_XORParity - cnt_noParity - PPC")
# for xtalk_i in xtalkCnt_FTF_rec_dict.keys():
#     print("{} - {} - {} - {} - {}".format(xtalk_i,
#                                           xtalkCnt_FTF_rec_dict[xtalk_i],
#                                           xtalkCnt_XOR_rec_dict[xtalk_i],
#                                           xtalkCnt_noParity_rec_dict[xtalk_i],
#                                           xtalkCnt_PPC_rec_dict[xtalk_i]))
#
#
# print("HexArray:")
# print("xtalk - cnt_FTFParity - cnt_XORParity - cnt_noParity - PPC")
# for xtalk_i in xtalkCnt_FTF_hex_dict.keys():
#     print("{} - {} - {} - {} - {}".format(xtalk_i,
#                                           xtalkCnt_FTF_hex_dict[xtalk_i],
#                                           xtalkCnt_XOR_hex_dict[xtalk_i],
#                                           xtalkCnt_noParity_hex_dict[xtalk_i],
#                                           xtalkCnt_PPC_hex_dict[xtalk_i]))

######################################################
n_checkPeriod = 100
n_dataCycle = 8

simu_instance = XtalkLevelEvaluation.XtalkLevelEval()
cntInstance_FPF, cntInstance_XOR, cntInstance_noParity, cntInstance_PPC = simu_instance.runSimu_16x16Array_FPF(n_dataCycle=n_dataCycle,
                                                                                                               n_simuPeriod=n_checkPeriod)

xtalkCnt_FPF_rec_dict = cntInstance_FPF.get_cnt_rec()
xtalkCnt_FPF_hex_dict = cntInstance_FPF.get_cnt_hex()
xtalkCnt_XOR_rec_dict = cntInstance_XOR.get_cnt_rec()
xtalkCnt_XOR_hex_dict = cntInstance_XOR.get_cnt_hex()
xtalkCnt_noParity_rec_dict = cntInstance_noParity.get_cnt_rec()
xtalkCnt_noParity_hex_dict = cntInstance_noParity.get_cnt_hex()
xtalkCnt_PPC_rec_dict = cntInstance_PPC.get_cnt_rec()
xtalkCnt_PPC_hex_dict = cntInstance_PPC.get_cnt_hex()

print("RecArray:")
print("xtalk - cnt_FPFParity - cnt_XORParity - cnt_noParity - PPC")
for xtalk_i in xtalkCnt_FPF_rec_dict.keys():
    print("{} - {} - {} - {} - {}".format(xtalk_i,
                                          xtalkCnt_FPF_rec_dict[xtalk_i],
                                          xtalkCnt_XOR_rec_dict[xtalk_i],
                                          xtalkCnt_noParity_rec_dict[xtalk_i],
                                          xtalkCnt_PPC_rec_dict[xtalk_i]))


print("HexArray:")
print("xtalk - cnt_FPFParity - cnt_XORParity - cnt_noParity - PPC")
for xtalk_i in xtalkCnt_FPF_hex_dict.keys():
    print("{} - {} - {} - {} - {}".format(xtalk_i,
                                          xtalkCnt_FPF_hex_dict[xtalk_i],
                                          xtalkCnt_XOR_hex_dict[xtalk_i],
                                          xtalkCnt_noParity_hex_dict[xtalk_i],
                                          xtalkCnt_PPC_hex_dict[xtalk_i]))

