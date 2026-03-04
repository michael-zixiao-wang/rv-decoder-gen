## Makefile for generate decode verilog file from .csv file 

# top name
TOP_NAME = mrt64_decoder
TEMPLATE_FILE = ./template/mrt64_decoder_template.sv

# input csv source
CSV_PATH = ./csv_source
CSV_DEC_FILE = $(CSV_PATH)/rv-dec-table.csv
CSV_CSR_FILE = $(CSV_PATH)/rv-csr-table.csv
CSV_PRIV_FILE = $(CSV_PATH)/rv-priv-table.csv

# script source
SCRIPT_PATH = ./scripts
CSV2PLA4DEC_SCRIPT = $(SCRIPT_PATH)/csv2pla4dec.py
CSV2PLA4CSR_SCRIPT = $(SCRIPT_PATH)/csv2pla4csr.py
CSV2PLA4PRIV_SCRIPT = $(SCRIPT_PATH)/csv2pla4priv.py
GEN_WRAP_SCRIPT = $(SCRIPT_PATH)/gen_unified_wrapper.py
EMBED_SCRIPT = $(SCRIPT_PATH)/embed_decoder.py

# file (or module) name for pla generate or abc opt
DEC_NAME = dec_opt
CSR_NAME = csr_opt
PRIV_NAME = priv_opt

# define the ABC opt instruction
ABC_DEC_CMD = "read_pla $(DEC_NAME).pla; strash; balance; rewrite; refactor; balance; rewrite; rewrite -z; balance; print_stats; write_verilog $(DEC_NAME).sv"
# ABC_DEC_CMD = "read_pla $(DEC_NAME).pla; print_stats; write_verilog $(DEC_NAME).sv"
ABC_CSR_CMD = "read_pla $(CSR_NAME).pla; strash; balance; rewrite; refactor; balance; rewrite; rewrite -z; balance; print_stats; write_verilog $(CSR_NAME).sv"
ABC_PRIV_CMD = "read_pla $(PRIV_NAME).pla; strash; balance; rewrite; refactor; balance; rewrite; rewrite -z; balance; print_stats; write_verilog $(PRIV_NAME).sv"

# wrapper file name
WRAPPER_FILE = decoder_wrapper.v

# output folder
OUTPUT_FOLDER = vsrc

all: move
		@echo "Finish all the flow! Final target folder: vsrc"

move: gen_top
		@mkdir -p $(OUTPUT_FOLDER)
		@mv *.sv ./$(OUTPUT_FOLDER)/

gen_top: $(WRAPPER_FILE)
		@echo "generate verilog top module ..."
		python3 $(EMBED_SCRIPT) $(TEMPLATE_FILE) $(DEC_NAME).pla $(CSR_NAME).pla $(PRIV_NAME).pla

# generate the wrapper file
$(WRAPPER_FILE): abc
		@echo "generate verilog wrapper module ..."
		python3 $(GEN_WRAP_SCRIPT) $(DEC_NAME).pla $(CSR_NAME).pla $(PRIV_NAME).pla

# PLA -> Verilog 
abc: gen_pla
		@echo "generate verilog from .pla by abc ..."
		abc -c $(ABC_DEC_CMD)
		abc -c $(ABC_CSR_CMD)
		abc -c $(ABC_PRIV_CMD)

# csv -> pla
gen_pla: $(CSV_DEC_FILE) $(CSV2PLA4DEC_SCRIPT)  $(CSV_CSR_FILE) $(CSV2PLA4CSR_SCRIPT)  $(CSV_PRIV_FILE) $(CSV2PLA4PRIV_SCRIPT)
		@echo "translate .pla from .csv ..."
		python3 $(CSV2PLA4DEC_SCRIPT) $(CSV_DEC_FILE) $(DEC_NAME).pla
		python3 $(CSV2PLA4CSR_SCRIPT) $(CSV_CSR_FILE) $(CSR_NAME).pla
		python3 $(CSV2PLA4PRIV_SCRIPT) $(CSV_PRIV_FILE) $(PRIV_NAME).pla


clean:
		@echo "clean .pla and .v file"
		rm -f *.pla
		rm -rf $(OUTPUT_FOLDER)
		rm -f abc.history
