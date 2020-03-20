from typing import Any, Dict

constants: Dict[str, Any] = {
    "NUMBER_OF_HEADS": 3,  # The number of tips each full node keeps track of and propagates
    "DIFFICULTY_STARTING": 500,  # These are in units of 2^32
    "DIFFICULTY_FACTOR": 3,  # The next difficulty is truncated to range [prev / FACTOR, prev * FACTOR]
    # These 3 constants must be changed at the same time
    "DIFFICULTY_EPOCH": 128,  # The number of blocks per epoch
    "DIFFICULTY_WARP_FACTOR": 4,  # DELAY divides EPOCH in order to warp efficiently.
    "DIFFICULTY_DELAY": 32,  # EPOCH / WARP_FACTOR
    "SIGNIFICANT_BITS": 12,  # The number of bits to look at in difficulty and min iters. The rest are zeroed
    "DISCRIMINANT_SIZE_BITS": 1024,  # Max is 1024 (based on ClassGroupElement int size)
    "BLOCK_TIME_TARGET": 300,  # The target number of seconds per block
    # The proportion (denominator) of the total time that that the VDF must be run for, at a minimum
    # (1/min_iters_proportion). For example, if this is two, approximately half of the iterations
    # will be contant and required for all blocks.
    "MIN_ITERS_PROPORTION": 10,
    # For the first epoch, since we have no previous blocks, we can't estimate vdf iterations per second
    "MIN_ITERS_STARTING": (2 ** 17),
    "MAX_FUTURE_TIME": 7200,  # The next block can have a timestamp of at most these many seconds more
    "NUMBER_OF_TIMESTAMPS": 11,  # Than the average of the last NUMBEBR_OF_TIMESTAMPS blocks
    # If an unfinished block is more than these many seconds slower than the best unfinished block,
    # don't propagate it.
    "PROPAGATION_THRESHOLD": 300,
    # If the expected time is more than these seconds, slightly delay the propagation of the unfinished
    # block, to allow better leaders to be released first. This is a slow block.
    "PROPAGATION_DELAY_THRESHOLD": 1500,
    # Hardcoded genesis block, generated using tests/block_tools.py
    # Replace this any time the constants change.
    "GENESIS_BLOCK": b'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x15N3\xd3\xf9H\xc2K\x96\xfe\xf2f\xa2\xbf\x87\x0e\x0f,\xd0\xd4\x0f6s\xb1".\\\xf5\x8a\xb4\x03\x84\x8e\xf9\xbb\xa1\xca\xdef3:\xe4?\x0c\xe5\xc6\x12\x80\x88\xbe_6 X\xf1\x83\xe8\x99\xdf)\xb8\xf6t\xe0;\x82\x17\xc5\xe5\x94\xb7\xef\xc2|\x94\xe6\xfb\x91L\x85\xe4\x00WVV\xefJ\x1e/>\xf6\xc5Gr5n\x13\x00\x00\x00\x98\xe4\xd8(mep\xcf}\xdb\xd7(\x04N"\xd1I\x18g\xae[\xff\xc0#z\xee\xb7\xbd3f\xe4zR3mi-\x89\x88\xbc\xd3\xf0|\xee\x03\x13\xc9}\xbb\x9b\x7f\x7f\xcfj\x08\x01\xe0*\x1e\x9an\xf6\xba\xd5\xb1\xc1\x80\x96\x8a\x99\xe3\x91\x92j\xce\xfdij\xea\xccT\xd0[\xd0\x89\xdc\xb8\xa3 /\xf27\x0f\x9ce\x87\x9dK\xe7\xab\x01\xbb\x1e\x91U\x95\x0f\xc0c\xa3\xa4\x81Um\x80_\xee\x8f3\xc7\xe3?\xf5\xacyF\x941\x90\x9e\xd1\xd0\x0bB\xa4\xa4\xe18\x13\xd5x\xca\xbd\x9b;\xf9B\xa1y\xaasm\x14\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x03\xaf\x99\x00I\x998~\xb9\x8e;\xed:\x19M\xcfp.\xd3A#8a\xb8\x9eee\xda\xfa\xff\xbc\x1ea\xcfN\xda\xde\x02\xe0\xc0\'3\xe41\x8b\xec\xda<@\xb4\x14,\xb5X)\xdbI\xdcS\xe8/\xfa$\n\xaf\xa6\xe0\xce\xff\xd0\x93x`\xb11\xc4\xa2I\xe1-\xd5\x1c\xc7\xef\x88\x05\xa8\x7f\xddp\x8ak\n\xa3\x96\x80L\xefV\xa2\x82\xfa\x92I\x14\x93\xb6\xfbW\n\xcf=W]\xcb\xc5\x0bf\xce4\x1d]\xb6"\t\x07\x82\x9f\xafq{D5\x03\x00\x00\x03\xa6\x00\x1a\x94\xcf\x9c\xe2{;\xd1\x97\x1dg\'\xb7\x08\xff\xb0,b.\xf0\xf7\x17;\x03\xb1\xe3\xf0\x10\xb7\xb9ov\xde\x9e\x0f4\xd4\xe9\xcf0\xb4\xf7\x07BJ\xb2IGz#\xa3\x90\xbd\x04\xaeI^>\xe86\xf0\x1f\x90b\xff\xe5\xb4\xd33\xd8\x1e\xdc\xdd\xcc\xfa\xf9\x9a\xf6L\xbd\xe98\xf5\'\xb6W\x83\xfa\xee\xb5/>U\xe6\xdf;C\x9e!\x9d[h\x12\xeb\xecg\xa9j\x96$"HB&\x93\xf9\x1e\xc6\xedO\xab\x9c:T8z\xcdQe\x00\x00\x00\x00\x00\x00\x148\x00^\x0b\xe4\x131\xb2\x19\x0e\x148\x82\x94\xdbu\x1f\xd6\xdf\x18v\xf9\x87\xa6\xf8Jbw\x88&\xb0\x85\xd9\xc4B~a\x01Y\xda?JKN\xa1\xbc:\xb4:\xeb\x02Z\xd4g\xda\xed\x12\x0f.svA^\x82\x1a*\xff\xa2O\x0e[\xae\x916\xd6z\xf2+\xc8&Jg\xec\x93g\x98\xb14\x10\xb1\xd0$s\rLw2\x8cCm\x01Q\x81\xf6f\xae\x9b\xee\x89\xe1I\x16\x91\xa7eF\x88"O\x1b\x85k,\xf5\xb2\xb5\xbd\xd8=\xb6}\x00\t\xef\xfd\x15P\x18\xb8\xc9\xb4\x9a\x8b^\xd9\xd3\xf6\x13\xbf\x9d\x10\xe6%\xcdL9L\xf5\xc2dP\x9b\x006\xf1&Eo9\x18\xda\x82!Q\x10\x1e\x9b\x08S\x08i\xb8\x17\xb3mP\xd7\xaa\x9b\xbd@F\xe5X{\xe8\x00\x06\'N\xf1\x00Hh\xdf G4\xa5N`L!\xcah\xd0\x9fv]\xfb\x00F\xb4n\xeb8c\xc3\x08\x14\xc2\xa8\xe4v\xf6M\xd0\x06\xb8\xe2\x01Z\r7\x17\xe5\xdbq\x8d\xec\xd5\xb2CJ\xbe> \x1b\x12v\xa1\x00\x00\x00\x00\x00\x00k\xd7\x00%\x0f\xfd\xc6R&\xb4\x12G\x84\x0bM\xae^\x84)\xcaI\xd5\xdf\xbc~\xb8CK\xd72;\x1a4<\xe9\x91(\x01\xe1\x00\xbf\x15\xb13A\xc5\xc8\xb2u\x9a)@\xc41M|X\x9aY\xc1h-\xeadI\x1d\xa0\xff\xf1\xc3\xfa\xde\xd6\xb1\x15U\n\xf9;\x94\xd4\xe0\x0fz\xb9\xf7\xa3\xcc\x9enr\x02<\x83\x9d@\x8b;\xbb@Z\x86\xe6\xcb\xb0J\xe9\x0c\xae\xc7L\xf3<\x0f$\xd2C\x1elD\xa4\x18\x1e@\xa9\x80\xbdcn]/\x01\x00\x08!il\xd5\x81,5}I\xde\\Z_!\t\x8c\xcftL\x0b*\xcdZ\xa2u\xaf\x00M\xf6ja\xb8 \r\xe3\xde\xcd\xae\xe0\x8e\x82(\xf0\xaa\xdf*o\xdb\x91L\x8e\xd4U\x94\xe3\xa4# \x1eO\xa3\t\xe2\xff\xf9\xf0\xbf\xc2A\xbd\xab\xdb\xbb\x05\xe7\xa6\xee\xa0\xc4\xb4\x12\xb3\xf7\x97#\x8b\xd0\xf5,L5\xbe\x96\xb6T\xd6\xd6\xb1/ \xef\x0fM;\xc5\x8b\x94\x93\xe4k\x89O\r\xb9c\xca\x1c\x99\xe0<C]w\x97K\xdd\xf7\xad\x00\x00\x00\x00\x00\x03(\xcc\x00My7\xf2\xf0\xf8\x98>\xc7\x91\xfa\xa7}~s\xf7=\xcb\x0c\x1a,\xa7\x15WV\x1a\xbec\xdc\xb6R\xafj\xe0\x07\xc9\xde\xcf\xddn\xcb\xb5\x9e\xaa\xb1Fh.\x8f\xe7\x1cc\x06b\x85\xc1(t\x8d\xaf\xef\x84\xcf\xf4\x00!\x03\xd6P\x03\xbf\xf1\x96#\x12k\xaa\xc4\xef\xd9\x89\xba`i\x0b\xc8\xb9?\xa3\xa4\xafo\x03\\cG\xc7\xaa\xf5\x02\x98\xad(\xd1\xb3\xbc3\x00\x84y4\x1aso_A\xf3q\xcd\xa1\xa2\xf8\x87v\x84z\xac\xab_\x00`\xa3\xb0c\xc9Dx\x0e\xb8\xb35\x1c\xc8L\xd9\x1aE\xce$\xf9\x0b\xf0-\x00\xb6\xaei\xd0>\xc9\xf4{\xb0\xa9\\\x04cls\xd7\xee\xf6Yw\x19v\x0c\x90\xc7\xdb\xec\xe3q\x9et2"kX\xd8\x91\xe2L\x03\xff\xb7\xb1\x95U\x84_"*\xa4S"\x1b\x98\x98\xb6\xf6 \x1a\x7f\x9e\x9d\xd7\xca@\xc3*\x95\xad4\x8c\xc9\xcb\x01\x1b\x80\xd4\x08\xa1\xba\xca8\t]\xff\xa4\x1ai4\x13?Le\xf1A\xad\x15?\xd5\xa8\x7f\xc4\xab\xdc\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^tka\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x93h\xb0E\x0c\xaa\xda1\x9a\x04\x83 \xedGe\xf1\'\xab\xc7Z\x9d\xaf!\x18D#\t\x0bz\xe2\xc4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf4\x00\x00\x00\x00\x00\x03\xaf\x99\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8b)\xaa\x96x8\xd76J\xa6\x8b[\x98\t\xe0\\\xe3^7qD\x8c\xf5q\x08\xf2\xa2\xc9\xb03mv\x00\x00\x0c\xbb\xa1\x06\xe0\x00N\x1f\xe8;}6F\xd7\xec\xc7\x83\x16T\x96\x1f\xe6\x88,\xa4\x9b\xa3Lo\xd0\xe6\x89jW\xac\xba\xae)\xe9\x91?\x97\x0fU\xf5\xd8\xdc\x9e\xce\xbf~\xad\xc2\xbc\x17v|\x947N\x0e\xfa\xff\xe6;\xce@|\xe9{\xe2:\xa8H\xb4\xb9\xde;<;-\x9a\x03\xbf\xa3\xff\xed\x81\x0cd\x80|(I\x9e\x8c\xa5\x83\xdf\x8a\x1aX\xc1#\x19uE`)\xeblV\x1d\x8f\xe6\x1f\xfa\x03\xe2\xf4b\xdfO\x9c\x11\x1fHJ2\xbfvC\x8b^\x8b)\xaa\x96x8\xd76J\xa6\x8b[\x98\t\xe0\\\xe3^7qD\x8c\xf5q\x08\xf2\xa2\xc9\xb03mv\x00\x00\x01\xd1\xa9J \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$)\xcf\x82\xc23&\xedzR\x04\xb8Zz\xe9\x03\x94\xe1\x0f\xc2\xe1TS\xc2\xb6\xd1\xa5\xf2\xd6\xb4\xae\xfb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xca\x92\\\xcf\xab\x03\xc7\x84\xdb\xc2q\xe1\xb3\xdaB\x18\x9c"\xb4\xd49Z\xe4{\xa7&q<\x18"\xf7\xbb\x9d\xe1\x07\x82v|\xf0!\xef\x17\xb73\xf3+X#\x0f\x99%Q0\x93}\xa4\xec\n\xc0\xf6\xaf\xdb\xff\xecxyfVB\xb4\x92\xe8a\xb9LN\xe5\xb5|-\xe2\xca\xaf\xd0\x8e\xfe\xaa9\xb5\xb1\xe0\xf1\x9c>\xdb\x92\x00\x00',  # noqa: E501
    # Target tx count per sec
    "TX_PER_SEC": 20,
    # Size of mempool = 10x the size of block
    "MEMPOOL_BLOCK_BUFFER": 10,
    # Coinbase rewards are not spendable for 200 blocks
    "COINBASE_FREEZE_PERIOD": 200,
    # Max coin amount int(1 << 48)
    "MAX_COIN_AMOUNT": 281474976710656,
    # Raw size per block target = 1,000,000 bytes
    # Rax TX (single in, single out) = 219 bytes (not compressed)
    # TX = 457 vBytes
    # floor(1,000,000 / 219) * 457 = 2086662 (size in vBytes)
    # Max block cost in virtual bytes
    "MAX_BLOCK_COST": 2086662,
}
