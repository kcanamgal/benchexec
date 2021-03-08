# This file is part of BenchExec, a framework for reliable benchmarking:
# https://github.com/sosy-lab/benchexec
#
# SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import benchexec.util as util
import benchexec.tools.template
import benchexec.result as result


class Tool(benchexec.tools.template.BaseTool2):
    
    #Needed for benchexec to run, but irrelevant for p4 extension
    def executable(self, tool):      
        return "/"
        
    def name(self):
        return "P4 Test"

    def determine_result(self, run):
        for line in run.output:
            if run.cmdline[3] + " ... ok" in line:
                return benchexec.result.RESULT_CLASS_TRUE
            else:
                return benchexec.result.RESULT_CLASS_FALSE
            