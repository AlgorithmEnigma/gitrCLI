use reqwest::header::USER_AGENT;
use serde::Deserialize;
use serde_json;
use std::collections::HashMap;
use std::error::Error;
use std::fs::File;
use std::io::BufReader;
use std::path::Path;
use structopt::StructOpt;

#[derive(StructOpt)]
struct CLI {
    url: String,
}

#[derive(Deserialize, Debug)]
struct Key {
    user: String,
    auth: String,
}

// #[derive(Deserialize, Debug)]
// struct Res {

// }

fn read_key_from_file<P: AsRef<Path>>(path: P) -> Result<Key, Box<dyn Error>> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    // println!("{:?}", reader);
    let key = serde_json::from_reader(reader)?;

    Ok(key)
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = CLI::from_args();
    // let key = read_key_from_file("keys.json").unwrap();
    // println!("{:?}", key.user);

    let client = reqwest::Client::builder().build()?;

    let res = client
        .get(format!("{}", args.url))
        .header(USER_AGENT, "gitr")
        .send()
        .await?;
    // .json()
    // .await?;

    let t = res.text().await?;
    // println!("{:?}", t);

    let json: serde_json::Value = serde_json::from_str(&t)?;

    println!("{:?}", json);
    // let resp = reqwest::get(format!("{}", args.url)).await?;
    // .json::<HashMap<String, String>>()
    // .await?;
    // println!("{:#?}", resp);
    Ok(())
}
