// IIRCoeffs : coefficients (b0, b1, b2, a0, a1, a2) for N_SOS_SECTIONS cascaded SOS sections
#define IIR_QXY_RES_NBITS 13 // Q2.13
#define N_SOS_SECTIONS 4
int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {
{ 7005, -13319, 7005, 8192, -15164, 7877},
{ 8192, -15593, 8191, 8192, -15427, 7917},
{ 8192, -15560, 8192, 8192, -15466, 8155},
{ 8192, -15606, 8192, 8192, -15628, 8159},
};
int32_t IIRu[N_SOS_SECTIONS] = {0}, IIRv[N_SOS_SECTIONS] = {0};
