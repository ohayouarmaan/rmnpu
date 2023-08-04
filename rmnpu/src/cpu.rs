use std::collections::HashMap;
use crate::memory;

pub enum Instructions {
    MOV_LITERAL_R1,
}

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

    pub fn fetch_16bites(&mut self) -> u16 {
        let current_ip_value = self.get_register("ip");
        let ins = self.memory.mem[current_ip_value as usize];
        self.set_register("ip", current_ip_value + 1);
        return ins;
    }


    pub fn set_register(&mut self, name: &str, value: u16) -> &mut Self {
        match self.register_map.get(name) {
            Some(ke) => {
                self.register.mem[*ke] = value;
            },
            _ => {
                panic!("Can't assign.");
            }
        }
        return self;
    }

    pub fn get_register(&self, name: &str) -> u16 {
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
    pub fn execute(&mut self, ins: Instructions) {
        match ins {
            Instructions::MOV_LITERAL_R1 => {
                let lit_value = self.fetch_16bites();
                self.set_register("r1", lit_value);
            }
        }
    }

    pub fn step(&mut self) {
        self.set_register("ip", 0x00);
        let ins = self.fetch_16bites();
        let mut ins = match ins {
            0x00 => {
                Instructions::MOV_LITERAL_R1
            }
            _ => {
                panic!("wtf");
            }
        };
        self.execute(ins);
    }

}