use std::collections::HashMap;
use crate::memory;

#[derive(Debug)]
pub struct cpu {
    pub memory: memory::memory,
    pub register_map: HashMap<String, usize>, 
    pub register: memory::memory
}

impl cpu {
    pub fn new(mem: memory::memory) -> Self {
        let mut registers = HashMap::new();
        let regs = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "ip", "acc"];
        for (i, s) in regs.iter().enumerate() {
            registers.insert(String::from(*s), i);
        }

        let mut c = Self {
            memory: mem,
            register_map: registers,
            // 10 registers of 16 bytes -> 160 bytes and since we are using u8 it should be 360
            register: memory::memory::new(160)
        };
        return c;
    }

    pub fn fetch(self, addr: usize) -> u16 {
        self.memory.mem[addr]
    }


    pub fn set_register(&mut self, name: &str, value: u16) {
        match self.register_map.get(name) {
            Some(ke) => {
                self.register.mem[*ke] = value;
            },
            _ => {
                panic!("Can't assign.");
            }
        }
    }

    pub fn get_register(&mut self, name: &str) -> u16 {
        match self.register_map.get(name) {
            Some(ke) => {
                self.register.mem[*ke]
            },
            _ => {
                panic!("Can't assign.");
            }
        }
    }

    //TODO: Implement an enum with all the instructions
    pub fn decode(&self) {

    }

}