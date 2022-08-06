import m5

from gem5.components.boards.simple_board import SimpleBoard
from gem5.isas import ISA
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import CustomResource
from gem5.simulate.simulator import Simulator
from gem5.components.cachehierarchies.classic.\
    private_l1_cache_hierarchy import (
    PrivateL1CacheHierarchy,
)
from gem5.components.processors.cpu_types import(
    get_cpu_types_str_set,
    get_cpu_type_from_str,
)

import argparse

parser = argparse.ArgumentParser(
        description = "cpu model"
)
parser.add_argument(
    "-n",
    "--num-cpus",
    type=int,
    choices=(1, 2, 4, 8),
    required=True,
    help="The number of CPUs.",
)
parser.add_argument(
    "-c",
    "--cpu",
    type=str,
    choices=get_cpu_types_str_set(),
    required=True,
    help="The CPU type.",
)
args = parser.parse_args()

cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="16kB", l1i_size="16kB")
memory = SingleChannelDDR3_1600("1GiB")

# isa=ISA.X86
# isa=str(m5.defines.buildEnv['TARGET_ISA']).lower(),
processor = SimpleProcessor(
    cpu_type=get_cpu_type_from_str(args.cpu),
    isa=ISA.X86,
    num_cores=args.num_cpus,
)

motherboard = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

binary = CustomResource("./x86_bin/tb32-static")
motherboard.set_se_binary_workload(binary)

simulator = Simulator(board=motherboard)
simulator.run()
