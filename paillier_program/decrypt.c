/*
 * decrypt.c
 *
 *
 *      Author: sourunsheng
 */

#include <stdlib.h>
#include <stdio.h>
#include <gmp.h>
#include "paillier.h"
#define BASE 32

int main(int argc, char*argv[]){
	paillier_pubkey_t *pubkey;
	paillier_prvkey_t *privkey;

	paillier_ciphertext_t ciphertext_input;
	paillier_plaintext_t output;
	mpz_init(ciphertext_input.c);
	mpz_init(output.m);

	pubkey = paillier_pubkey_from_hex("8b7401f20812b8a58678f4c9f73f3b7f");
	privkey = paillier_prvkey_from_hex("45ba00f904095c520637a615b99fb088",pubkey);

	if(argc == 2){
		mpz_set_str(ciphertext_input.c, argv[1], BASE);
		paillier_dec(&output, pubkey, privkey, &ciphertext_input);
		unsigned long dec_res = mpz_get_ui(output.m);
		printf("%lu\n",dec_res);
		return dec_res;
	}
	else if(argc>2){
		printf("Too many inputs.\n");
		return 1;
	}
	else{
		printf("Need at least one input.\n");
		return 1;
	}
}
