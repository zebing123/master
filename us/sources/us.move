module us::us;
use std::string;
use sui::transfer::transfer;
use std::string::String;
use sui::tx_context::sender;
public struct US has key{
    id:UID,
    name:String,
    image_url:String,





}

public entry fun Mint(url:String,ctx: &mut TxContext){

    let us = US{
        id:object::new(ctx),
        name:string::utf8(b"it is a try"),
        image_url:url
    };

    transfer(us,sender(ctx));
}


