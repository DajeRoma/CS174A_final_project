/*
 * encrypt.c
 *
 *  Created on: 2015年12月6日
 *      Author: sourunsheng
 */
#include <stdlib.h>
#include <stdio.h>
#include <gmp.h>
#include "paillier.h"
#define BASE 32

int main(int argc, char * argv[]){
	// encrypt input numeric value
	paillier_pubkey_t *pubkey;
	paillier_prvkey_t *privkey;
	paillier_ciphertext_t ciphertext1;
	mpz_init(ciphertext1.c);
	int input_v;
	sscanf (argv[1],"%d",&input_v);
	if (argc == 2) {
		pubkey = paillier_pubkey_from_hex("8b7401f20812b8a58678f4c9f73f3b7f");
//		privkey = paillier_prvkey_to_hex("45ba00f904095c520637a615b99fb088");
		paillier_plaintext_t* input1 = paillier_plaintext_from_ui(input_v);
//		gmp_printf("Here is the original value one: %Zd\n", input1->m);

		paillier_enc(&ciphertext1, pubkey, input1, &paillier_get_rand_devurandom);
		char * encrypted_res= mpz_get_str(NULL, BASE, ciphertext1.c);
		printf("%s\n", encrypted_res);
		return 0;
	}
	else if (argc >2){
		printf("Too many input.\n");
		return 1;
	}
	else{
		printf("One argument expected.\n");
		return 1;
	}
}

