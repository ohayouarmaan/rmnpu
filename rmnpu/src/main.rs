mod memory;
mod cpu;

fn main() {
    let mut m = memory::memory::new(2048);
    m.mem[0] = 0x00;
    m.mem[1] = 0xFF;
    let mut c = cpu::cpu::new(m);
    println!("current r1 value: {}", c.get_register("r1"));
    c.step();
    println!("current r1 value: {}", c.get_register("r1"));
}
