uint32_t CRC32::calculate(CircularBuffer *buffer, uint16_t start, uint16_t size)
{
    uint32_t crc = ~0;
    uint16_t index, i;
    for (i = 0, index = start; i < size; i++, index++)
        crc = _table[(crc ^ buffer->read(index)) & 0xFF] ^ (crc >> 8);
    return ~crc;
}
