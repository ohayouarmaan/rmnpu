mod memory;
mod cpu;

fn main() {
    let mut m = memory::memory::new(2048);
    let mut i = 0;

    m.mem[i] = 0x00;
    i += 1;
    m.mem[i] = 0xF1;
    i += 1;
    m.mem[i] = 0x02;
    i += 1;
    m.mem[i] = 0x03;
    i += 1;
    m.mem[i] = 0x01;

    let mut c = cpu::cpu::new(m);
    c.debug();
    c.step();
    c.debug();
    c.step();
    c.debug();
}
