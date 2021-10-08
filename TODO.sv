// 1. Automatically create connection to the coverage monitor

// 2. Can use uvm_callback to register the coverage monitor and sample the coverage object
    
    //=====================================================================================
    // base cb class
    class obj_cb extends uvm_callback;
        virtual function void pre_drive(transaction1); endfunction
        virtual function void post_drive(transaction2); endfunction
    endclass

    //=====================================================================================
    // user cb class
    class user_cb extends obj_cb;
        // cov_collector is the class that has all the covergroups that are generated
        cov_collector u_cov;

        virtual function void pre_drive(transaction1);
            u_cov.CoverObj1.sample(transaction1);
        endfunction

        virtual function void post_drive(transaction2);
            u_cov.CoverObj2.sample(transaction2);
        endfunction
    endclass

    //=====================================================================================
    // actual obj class that has will call the cb
    class obj extends uvm_component;
        `uvm_register_cb(obj, obj_cb)
        ...
        `uvm_do_callbacks(obj, obj_cb, pre_drive(transaction1))
        ...
        `uvm_do_callbacks(obj, obj_cb, post_drive(transaction2))
        ...
    endclass

    //=====================================================================================
    // test code that creates the callback, and add it to the registry
    class user_test extends uvm_test;
        user_cb u_cb = user_cb::type_id::create("my_cb");
        uvm_callbacks#(obj, obj_cb)::add(m_env.u_obj, u_cb);
    endclass

