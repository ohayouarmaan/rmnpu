#[derive(Debug)]
pub struct memory {
    pub mem: Vec<u16>
}

impl memory {
    pub fn new(size: usize) -> Self {
        Self {
            mem: vec![0u16; size]
        }
    }
}

impl Default for memory {
    fn default() -> Self {
        Self {
            mem: vec![0u16; 2048]
        }
    }
}
