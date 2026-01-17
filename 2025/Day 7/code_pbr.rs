use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

pub fn day07(file_loc: &str) {
    let inputs = get_input_arr(file_loc).unwrap();
    println!("---Day  7---");
    println!("Part 1: {}", p1(&inputs));
    println!("Part 2: {}", p2(&inputs));

}

fn get_input_arr<P>(filename: P) -> io::Result<Vec<Vec<i64>>>
    where P: AsRef<Path> {
        let file = File::open(filename)?;
        let reader = io::BufReader::new(file);
        let mut splits = Vec::new();

        for line in reader.lines(){
            let line = line?;
            splits.push(
                line.char_indices()
                    .filter(|(_, x)| *x == 'S' || *x == '^')
                    .map(|(i, _)| i as i64)
                    .collect()
            )
        }
        Ok(splits)
    }

fn p1(input: &Vec<Vec<i64>>) -> i32 {
    let mut splits = 0;
    let mut lasers = input[0].clone();
    for line in input[1..input.len()].into_iter(){
        let mut nextline = vec![];
        // This is slow but whatever
        for laser in lasers.into_iter(){
            if line.contains(&laser){
                nextline.push(laser-1);
                nextline.push(laser+1);
                splits += 1;
            } else {
                nextline.push(laser)
            }
        }
        nextline.dedup();
        nextline.sort();
        lasers = nextline;
    }
    return splits;
}

fn p2(input: &Vec<Vec<i64>>) -> i64 {
    let mut lasers = HashMap::new();
    lasers.insert(input[0][0], 1_i64);
    for line in input[1..input.len()].into_iter(){
        let mut nextline = HashMap::new();
        for (laser, ways) in lasers.iter(){
            if line.contains(laser){
                *nextline.entry(laser - 1).or_insert(0) += ways;
                *nextline.entry(laser + 1).or_insert(0) += ways;
            } else {
                *nextline.entry(*laser).or_insert(0) += ways;
            }
        }
        lasers = nextline;
    }
    return lasers.iter().map(|(_, i)| i).sum();
}

fn main() {
    day07("input.txt");
}