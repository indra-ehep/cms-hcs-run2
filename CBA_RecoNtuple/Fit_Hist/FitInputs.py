import ROOT as rt
#-----------------------------------------------------------------
condorCBADir  = "/eos/uscms/store/user/rverma/Output/cms-hcs-run2/CBA_RecoNtuple"
condorHistDir = "%s/Hist_Ntuple"%condorCBADir
#-----------------------------------------------------------------
Year 	      =	["2016", "2017", "2018"]
#Year 	      =	["2016"]
Channel 	  =	["Mu", "Ele"]
#Channel 	  =	["Mu"]
#Decay 	  =	["Semilep", "Dilep"]
Decay 	  =	["Semilep"]
Mass      = ["080", "090", "100", "120", "140", "150", "155", "160"]
Systematics   =	["PU","MuEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr"]
#Systematics   =	["JER", "JECTotal"]
#Systematics   =	["PU","Q2"]
SystLevel     = ["Up", "Down"]
ControlRegion = []
#ControlRegion=["tight_a4j_a1b", "veryTight_a4j_a2b", "tight_a4j_e0b", "looseCR_a2j_e1b", "looseCR_a2j_a0b", "looseCR_a2j_e0b", "looseCR_e3j_a2b", "looseCR_e3j_e0b", "looseCR_e2j_e1b", "looseCR_e2j_e0j", "looseCR_e2j_e2b", "looseCR_e3j_e1b"]
