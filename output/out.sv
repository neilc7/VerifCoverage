covergroup CoverPort  ;
    hi_lo_port: coverpoint port  { 
        bins hi[] = {[8:$]} ; // Separate bin for each port starting from 8
        bins lo = {[0:3]} ; // 1 bin for port 0-3
        bins others = default ; // 1 bin for others (not hi or lo) 
    }
    even_odd_port: coverpoint port[0]  { 
        bins even = {0} ; 
        bins odd = {1} ;  
    }
    special_port: coverpoint port iff (port[3] == 1) { 
        wildcard bins portQOS1 = {4'b10??} ; // Sample with condition that bit 3 of port is 1
        wildcard bins portQOS2 = {4'b11??} ;  
    }
    invalid_port: coverpoint port  { 
        illegal_bins rsvd = {4'b1111, 4'b1000} ;  
    }
endgroup

covergroup CoverTrans  @(req_event);
    addr: coverpoint tr.addr iff (tr.valid) { 
        bins prot = {[8'h80:$]} ; 
        bins hi = {[8'h40:8'h7f]} ; 
        bins lo = {[8'h10:8'h3f]} ; 
        bins rsvd = default ;  
    }
    cmd: coverpoint tr.cmd iff (tr.valid) { 
        bins read = cmd_read_e ; 
        bins write = cmd_write_e ;  
    }
    cross addr, cmd  { 
        ignore_bins wr_prot = binsof(addr.prot) && binsof(cmd.write) ; // ignore bin for write to protected addr
        ignore_bins rd_lo = binsof(addr) intersect {[8'h00:8'h0f]} && binsof(cmd.read) ; // ignore read from subset of lo address 
    }
endgroup

covergroup CoverObj  with function sample(ObjCls obj);
    data0: coverpoint obj.data  {  
        option.weight = 0;
    }
    data1: coverpoint obj.getData1() iff (obj.existData1()) {  
        option.weight = 0;
    }
    cross data0, data1  { 
        bins data0lo_data1hi = binsof(data0) intersect {[0:3]} && binsof(data1) intersect {[4:7]} ; 
        bins data0hi_data1lo = binsof(data0) intersect {[4:7]} && binsof(data0) intersect {[0:3]} ;  
    }
endgroup

covergroup CoverParam (int burst_max) with function sample(int size);
    burst_size: coverpoint size  { 
        bins burst_1 = {1} ; 
        bins burst_some = {[2:burst_max-1]} with (burst_max >= 3); // only create bin of burst_max >= 3
        bins burst_max = {burst_max} with (burst_max >= 2); // only create bin of burst_max >= 2 
    }
endgroup

