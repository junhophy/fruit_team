
#import sys
#sys.path.append("../")
from ROOT import TFile, TCanvas, TPad

wf= open("py-fillrandom_via_py2.txt","w+")
#f = TFile("../py-fillrandom.root","READ");
f = TFile("root_tree_from_txt.root");

hist=f.Get("h1f");
Nbin = hist.GetNbinsX();

for ii in range(1,Nbin+1):
    bin_l = hist.GetBinLowEdge(ii)
    bin_width = hist.GetBinWidth(ii);
    bin_h = bin_l + bin_width;
    binCont = hist.GetBinContent(ii);
    wf.write("%f %f %f\n" %(bin_l,bin_h,binCont))

f.Close()
