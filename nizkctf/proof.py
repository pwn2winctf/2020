# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
import os
import pysodium
from base64 import b64encode, b64decode
from .challenge import Challenge
from .team import Team
from .cli.teamsecrets import TeamSecrets


def proof_open(team, proof):
    proof = proof.encode('utf-8')

    assert isinstance(team, Team)
    assert isinstance(proof, bytes)

    proof = b64decode(proof)

    claimed_chall = proof[2*64:].decode('utf-8')
    chall_pk = Challenge(claimed_chall).pk
    team_pk = team['sign_pk']

    membership_proof = pysodium.crypto_sign_open(proof, chall_pk)
    chall_id = pysodium.crypto_sign_open(membership_proof,
                                         team_pk).decode('utf-8')

    if claimed_chall != chall_id:
        raise ValueError('invalid proof')

    return chall_id


def proof_create(chall_id, chall_sk):
    chall_id = chall_id.encode('utf-8')

    assert isinstance(chall_id, bytes)
    assert isinstance(chall_sk, bytes)

    team_sk = TeamSecrets['sign_sk']

    membership_proof = pysodium.crypto_sign(chall_id, team_sk)
    proof = pysodium.crypto_sign(membership_proof, chall_sk)

    return b64encode(proof).decode('utf-8')