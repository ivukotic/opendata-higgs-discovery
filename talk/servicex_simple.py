
from func_adl_servicex import ServiceXSourceUpROOT
ggH125_ZZ4lep = 'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root',
ggH125_ZZ4lep_source = ServiceXSourceUpROOT([ggH125_ZZ4lep], 'mini', 'uproot-af')
r = (ggH125_ZZ4lep_source.Select(lambda e: {'lep_pt': e['lep_pt']}).AsAwkwardArray().value()
     )
