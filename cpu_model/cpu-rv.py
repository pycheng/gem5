import m5

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.\
    private_l1_cache_hierarchy import (
    PrivateL1CacheHierarchy,
)
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import CustomResource
from gem5.simulate.simulator import Simulator

import argparse

cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="16kB", l1i_size="16kB")
memory = SingleChannelDDR3_1600("1GiB")
processor = SimpleProcessor(
    cpu_type=CPUTypes.TIMING,
    num_cores=1
)

motherboard = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

binary = CustomResource("/home/pycheng/gem5/gem5/tests/test-progs/hello/bin/riscv/linux/hello")
motherboard.set_se_binary_workload(binary)

simulator = Simulator(board=motherboard)
simulator.run()
