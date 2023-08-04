mod memory;
mod cpu;

fn main() {
    let m = memory::memory::new(2048);
    let mut c = cpu::cpu::new(m);
    c.set_register("ip", 0xFF);
}
