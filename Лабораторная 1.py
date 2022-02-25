def xor_cipher( str, key ):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return  encript_str    
 
strg = "Hello world"
key  = 8
print( "original:\t", strg )
encr_strg = xor_cipher( strg, key ) 
print( "encript:\t", encr_strg )
print( "decript:\t", xor_cipher( encr_strg, key ) )

