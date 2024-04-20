To verify how the flag is hidden, you can open up `Stegsolve.jar` and check the bit planes specially, the alpha channel hinted in the challenge name.

Then, `zsteg` can find the hidden data.
> `zsteg chal.png 1b,a,msb,yx`
> 
> seacrh the lsb, in the alpha channel in big endian format with vertical pixel order.

Or just run `zsteg -a chal.png` and search for the flag.

## Flag
> iutctf{bruh_7h47_w45_345y}
