import CACParitySeq_EncoderCore as CACParitySeq_EncoderCore

### FTF Codec Core
enc_result = CACParitySeq_EncoderCore.FTFParity_EncoderCore(seq_c=(1, 1, 1, 1, 1, 1),
                                                            seq_d=(0, 0, 1, 1, 1, 0))
print(enc_result)

enc_result = CACParitySeq_EncoderCore.FTFParity_EncoderCore(seq_c=(1, 1, 1, 0, 1, 1),
                                                            seq_d=(0, 0, 1, 1, 1, 0))
print(enc_result)