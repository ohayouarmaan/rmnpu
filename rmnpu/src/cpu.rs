use std::collections::HashMap;
use crate::memory;

pub enum Instructions {
    MOV_LITERAL_R1,
    MOV_LITERAL_R2,
    ADD_LITERAL,
    ADD_REG_REG,
    JMP_IF_NOT_EQ
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
        c.set_register("ip", 0x00);
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
            },
            Instructions::MOV_LITERAL_R2 => {
                let lit_value = self.fetch_16bites();
                self.set_register("r2", lit_value);
            },
            Instructions::ADD_LITERAL => {
                let lit_value = self.fetch_16bites();
                let register = self.fetch_16bites();
                match register {
                    0x00 => {
                        let current_value = self.get_register("r1");
                        self.set_register("r1", current_value + lit_value);
                    },
                    0x01 => {
                        let current_value = self.get_register("r2");
                        self.set_register("r2", current_value + lit_value);
                    },
                    _ => {
                        panic!("No such register available");
                    }
                }
                self.set_register("r2", lit_value);
            },
            Instructions::ADD_REG_REG => {
                let reg_1 = self.fetch_16bites();
                let reg_2 = self.fetch_16bites();
                self.set_register("acc", reg_1 + reg_2);
            },
            Instructions::JMP_IF_NOT_EQ => {
                let value = self.fetch_16bites();
                let address = self.fetch_16bites();
                if value != self.get_register("acc") {
                    self.set_register("ip", address);
                };
            },
            _ => {
                panic!("not able to execute.");
            }
        }
    }

    pub fn debug(&self) {
        println!("r1: {}\tr2: {}", self.get_register("r1"), self.get_register("r2"));
    }

    pub fn step(&mut self) {
        let ins = self.fetch_16bites();
        let ins = match ins {
            0x00 => {
                Instructions::MOV_LITERAL_R1
            },
            0x01 => {
                Instructions::MOV_LITERAL_R2
            },
            0x02 => {
                Instructions::ADD_LITERAL
            },
            0x03 => {
                Instructions::ADD_REG_REG
            }
            _ => {
                panic!("wtf");
            }
        };
        self.execute(ins);
    }

}