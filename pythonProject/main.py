import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import java.util.Arrays;
import java.util.Scanner;

public class kuz_ofb {
     static final byte[] pi = {
            (byte) 0xFC, (byte) 0xEE, (byte) 0xDD, 0x11, (byte) 0xCF, 0x6E, 0x31, 0x16,
            (byte) 0xFB, (byte) 0xC4, (byte) 0xFA, (byte) 0xDA, 0x23, (byte) 0xC5, 0x04, 0x4D,
            (byte) 0xE9, 0x77, (byte) 0xF0, (byte) 0xDB, (byte) 0x93, 0x2E, (byte) 0x99, (byte) 0xBA,
            0x17, 0x36, (byte) 0xF1, (byte) 0xBB, 0x14, (byte) 0xCD, 0x5F, (byte) 0xC1,
            (byte) 0xF9, 0x18, 0x65, 0x5A, (byte) 0xE2, 0x5C, (byte) 0xEF, 0x21,
            (byte) 0x81, 0x1C, 0x3C, 0x42, (byte) 0x8B, 0x01, (byte) 0x8E, 0x4F,
            0x05, (byte) 0x84, 0x02, (byte) 0xAE, (byte) 0xE3, 0x6A, (byte) 0x8F, (byte) 0xA0,
            0x06, 0x0B, (byte) 0xED, (byte) 0x98, 0x7F, (byte) 0xD4, (byte) 0xD3, 0x1F,
            (byte) 0xEB, 0x34, 0x2C, 0x51, (byte) 0xEA, (byte) 0xC8, 0x48, (byte) 0xAB,
            (byte) 0xF2, 0x2A, 0x68, (byte) 0xA2, (byte) 0xFD, 0x3A, (byte) 0xCE, (byte) 0xCC,
            (byte) 0xB5, 0x70, 0x0E, 0x56, 0x08, 0x0C, 0x76, 0x12,
            (byte) 0xBF, 0x72, 0x13, 0x47, (byte) 0x9C, (byte) 0xB7, 0x5D, (byte) 0x87,
            0x15, (byte) 0xA1, (byte) 0x96, 0x29, 0x10, 0x7B, (byte) 0x9A, (byte) 0xC7,
            (byte) 0xF3, (byte) 0x91, 0x78, 0x6F, (byte) 0x9D, (byte) 0x9E, (byte) 0xB2, (byte) 0xB1,
            0x32, 0x75, 0x19, 0x3D, (byte) 0xFF, 0x35, (byte) 0x8A, 0x7E,
            0x6D, 0x54, (byte) 0xC6, (byte) 0x80, (byte) 0xC3, (byte) 0xBD, 0x0D, 0x57,
            (byte) 0xDF, (byte) 0xF5, 0x24, (byte) 0xA9, 0x3E, (byte) 0xA8, (byte) 0x43, (byte) 0xC9,
            (byte) 0xD7, 0x79, (byte) 0xD6, (byte) 0xF6, 0x7C, 0x22, (byte) 0xB9, 0x03,
            (byte) 0xE0, 0x0F, (byte) 0xEC, (byte) 0xDE, 0x7A, (byte) 0x94, (byte) 0xB0, (byte) 0xBC,
            (byte) 0xDC, (byte) 0xE8, 0x28, 0x50, 0x4E, 0x33, 0x0A, 0x4A,
            (byte) 0xA7, (byte) 0x97, 0x60, 0x73, 0x1E, 0x00, 0x62, 0x44,
            0x1A, (byte) 0xB8, 0x38, (byte) 0x82, 0x64, (byte) 0x9F, 0x26, 0x41,
            (byte) 0xAD, 0x45, 0x46, (byte) 0x92, 0x27, 0x5E, 0x55, 0x2F,
            (byte) 0x8C, (byte) 0xA3, (byte) 0xA5, 0x7D, 0x69, (byte) 0xD5, (byte) 0x95, 0x3B,
            0x07, 0x58, (byte) 0xB3, 0x40, (byte) 0x86, (byte) 0xAC, 0x1D, (byte) 0xF7,
            0x30, 0x37, 0x6B, (byte) 0xE4, (byte) 0x88, (byte) 0xD9, (byte) 0xE7, (byte) 0x89,
            (byte) 0xE1, 0x1B, (byte) 0x83, 0x49, 0x4C, 0x3F, (byte) 0xF8, (byte) 0xFE,
            (byte) 0x8D, 0x53, (byte) 0xAA, (byte) 0x90, (byte) 0xCA, (byte) 0xD8, (byte) 0x85, 0x61,
            0x20, 0x71, 0x67, (byte) 0xA4, 0x2D, 0x2B, 0x09, 0x5B,
            (byte) 0xCB, (byte) 0x9B, 0x25, (byte) 0xD0, (byte) 0xBE, (byte) 0xE5, 0x6C, 0x52,
            0x59, (byte) 0xA6, 0x74, (byte) 0xD2, (byte) 0xE6, (byte) 0xF4, (byte) 0xB4, (byte) 0xC0,
            (byte) 0xD1, 0x66, (byte) 0xAF, (byte) 0xC2, 0x39, 0x4B, 0x63, (byte) 0xB6
    };

    static final int BLOCKLENGTH = 16;
    static final int KEYLENGTH = 32;

     static final byte[] Vector_a = {
            1, (byte) 148, 32, (byte) 133, 16, (byte) 194, (byte) 192, 1,
            (byte) 251, 1, (byte) 192, (byte) 194, 16, (byte) 133, 32, (byte) 148
    };

     static byte[][] roundConst = new byte[32][16];
     static byte[][] roundKey = new byte[10][64];

     public static void main(String[] args) throws InvalidKeySpecException, NoSuchAlgorithmException {
        Scanner in = new Scanner(System.in);
        String plain, encrypted, password;
        byte[] key, iv;
        System.out.println("E/D");
        String mode = in.nextLine();
        if (mode.equals("E")) { // при вводе сравниваем строки ecли E - enc если D - dec
            System.out.println("Name file");
            plain = in.nextLine();
            System.out.println("Encrypted file");
            encrypted = in.nextLine();
            System.out.println("password: ");
            String pass = in.nextLine();
            key = generationKey(pass); // генерим из пароля ключ для алгоритм шифрования
            generationIterKey(key); // генераируем итерационные ключм из ключа
            iv = generationIV(); // генераим вектор инициализации
            IVinFile(iv, encrypted); // записываем вектор инициализации в файл
            EncryptFile(plain, encrypted, iv); // передаем название файла для шифрования, название для гифрованного файла и вектор
        } else if (mode.equals("D")) {
            System.out.println("Encrypted file");
            plain = in.nextLine();
            System.out.println("Decrypted file");
            String dec = in.nextLine();
            System.out.println("password: ");
            password = in.nextLine();
            key = generationKey(password);
            generationIterKey(key);
            iv = IVfromFile(plain); // читаем вектор из файла
            DecryptFile(dec, plain, iv);
        } else {
            System.out.println("Wrong mode!");
        }
    }

     static byte[] XOR(byte[] leftBlock, byte[] rightBlock) { //  ксор блоков
        byte[] newBlock = new byte[BLOCKLENGTH];
        for (int i = 0; i < BLOCKLENGTH; i++)
            newBlock[i] = (byte) (leftBlock[i] ^ rightBlock[i]);
        return newBlock;
    }

     static byte[] SGOST(byte[] block) { // нелинейное преобразование
        int i;
        byte[] newBlock = new byte[block.length];
        for (i = 0; i < BLOCKLENGTH; i++) {
            int data = block[i];
            if (data < 0) {
                data = data + 256;
            }
            newBlock[i] = pi[data];
        }
        return newBlock;
    }

     static byte multiplyInGF(byte a, byte b) { // умножение в поле галуа
        byte c = 0;
        byte hi_bit;
        int i;
        for (i = 0; i < 8; i++) {
            if ((b & 1) == 1)
                c ^= a;
            hi_bit = (byte) (a & 0x80);
            a <<= 1;
            if (hi_bit < 0)
                a ^= 0x1c3; // = 451 = x^8+x^7+x^6+x+1
            b >>= 1;
        }
        return c;
    }

     static byte[] RGOST(byte[] block) { // сдвиг
        int i;
        byte a_15 = 0;
        byte[] temp = new byte[BLOCKLENGTH];
        for (i = 15; i >= 0; i--) {
            if (i == 0)
                temp[15] = block[i];
            else
                temp[i - 1] = block[i];
            a_15 ^= multiplyInGF(block[i], Vector_a[i]);
        }
        temp[15] = a_15;
        return temp;
    }

     static byte[] LGOST(byte[] block) { // линейное преоразваоние
        int i;
        byte[] newBlock;
        byte[] temp = block;
        for (i = 0; i < 16; i++) {
            temp = RGOST(temp);
        }
        newBlock = temp;
        return newBlock;
    }


     static void getConstGOST() {
        int i;
        byte[][] iterNum = new byte[32][16];
        for (i = 0; i < 32; i++) {
            for (int j = 0; j < BLOCKLENGTH; j++)
                iterNum[i][j] = 0;
            iterNum[i][0] = (byte) (i + 1);
        }
        for (i = 0; i < 32; i++) {
            roundConst[i] = LGOST(iterNum[i]);
        }
    }

     static byte[][] FGOST(byte[] keyOne, byte[] keyTwo, byte[] iterConst) {
        byte[] temp;
        byte[] out_key_2 = keyOne;
        temp = XOR(keyOne, iterConst);
        temp = SGOST(temp);
        temp = LGOST(temp);
        byte[] out_key_1 = XOR(temp, keyTwo);
        byte key[][] = new byte[2][];
        key[0] = out_key_1;
        key[1] = out_key_2;
        return key;
    }

     static void generationIterKey(byte[] key) { // генерим итерациооные ключи
        byte[] key_1 = new byte[BLOCKLENGTH];
        byte[] key_2 = new byte[BLOCKLENGTH];

        System.arraycopy(key, 0, key_1, 0, key_1.length);
        System.arraycopy(key, key_1.length, key_2, 0, key_2.length);
        int i;

        byte[][] iter12 = new byte[2][];
        byte[][] iter34;
        getConstGOST();
        roundKey[0] = key_1;
        roundKey[1] = key_2;
        iter12[0] = key_1;
        iter12[1] = key_2;
        for (i = 0; i < 4; i++) {
            iter34 = FGOST(iter12[0], iter12[1], roundConst[0 + 8 * i]);
            iter12 = FGOST(iter34[0], iter34[1], roundConst[1 + 8 * i]);
            iter34 = FGOST(iter12[0], iter12[1], roundConst[2 + 8 * i]);
            iter12 = FGOST(iter34[0], iter34[1], roundConst[3 + 8 * i]);
            iter34 = FGOST(iter12[0], iter12[1], roundConst[4 + 8 * i]);
            iter12 = FGOST(iter34[0], iter34[1], roundConst[5 + 8 * i]);
            iter34 = FGOST(iter12[0], iter12[1], roundConst[6 + 8 * i]);
            iter12 = FGOST(iter34[0], iter34[1], roundConst[7 + 8 * i]);

            roundKey[2 * i + 2] = iter12[0];
            roundKey[2 * i + 3] = iter12[1];
        }
    }

     static byte[] EncryptGOST(byte[] block) { // шифрование блока
        int i;
        byte[] newBlock;
        newBlock = block;
        for (i = 0; i < 9; i++) {
            newBlock = XOR(roundKey[i], newBlock);
            newBlock = SGOST(newBlock);
            newBlock = LGOST(newBlock);
        }
        newBlock = XOR(newBlock, roundKey[9]);
        return newBlock;
    }

    static void EncryptFile(String OriginalFile, String EncText, byte[] IV) {//шифрование файла
        File origFile = new File(OriginalFile);
        byte[] plainText = new byte[1];
        byte[] block;
        byte[] iv = IV;
        try {
            plainText = Files.readAllBytes(Paths.get(OriginalFile));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        int lastBytes = plainText.length % BLOCKLENGTH;
        byte[] encText = new byte[plainText.length + (BLOCKLENGTH - lastBytes)];
        for (int i = 0; i < plainText.length; i += BLOCKLENGTH) { // копируем файл в массив
            block = Arrays.copyOfRange(plainText, i, i + BLOCKLENGTH);
            iv = EncryptGOST(iv);
            block = XOR(block, iv);
            System.arraycopy(block, 0, encText, i, BLOCKLENGTH);
        }
        System.arraycopy(encText, 0, plainText, 0, plainText.length); // записываем шифрованный файл в текст
        try {
            Files.write(Paths.get(EncText), plainText, StandardOpenOption.APPEND, StandardOpenOption.CREATE); // запись в файл
        } catch (IOException e) {
            e.printStackTrace();
        }
        origFile.delete(); // удаление оригинального файла
    }

    static void DecryptFile(String OriginalFile, String EncryptFile, byte[] IV) {
        File vec = new File(EncryptFile + ".iv");
        File EncryptF = new File(EncryptFile);
        byte[] encText = new byte[1];
        byte[] block;
        byte[] iv = IV;
        try {
            encText = Files.readAllBytes(Paths.get(EncryptFile));//читаем весь в файл в массив
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        int lastBytes = encText.length % BLOCKLENGTH;
        byte[] decText = new byte[encText.length + (BLOCKLENGTH - lastBytes)];
        for (int i = 0; i < encText.length; i += BLOCKLENGTH) {
            block = Arrays.copyOfRange(encText, i, i + BLOCKLENGTH);
            iv = EncryptGOST(iv);
            block = XOR(block, iv);
            System.arraycopy(block, 0, decText, i, BLOCKLENGTH);
        }
        System.arraycopy(decText, 0, encText, 0, encText.length);
        try {
            Files.write(Paths.get(OriginalFile), encText, StandardOpenOption.APPEND, StandardOpenOption.CREATE);
        } catch (IOException e) {
            e.printStackTrace();
        }

        vec.delete();
        EncryptF.delete();
    }

     static byte[] generationKey(String Key) throws NoSuchAlgorithmException, InvalidKeySpecException { // генерация ключа
        byte[] temp = Key.getBytes();
        KeySpec spec = new PBEKeySpec(Key.toCharArray(), temp, 150, KEYLENGTH * 8);
        SecretKeyFactory f = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        return f.generateSecret(spec).getEncoded();
    }

     static byte[] generationIV() throws NoSuchAlgorithmException { //генерацтя вектора
        SecureRandom randomSecureRandom = SecureRandom.getInstance("SHA1PRNG");
        byte[] iv = new byte[BLOCKLENGTH];
        randomSecureRandom.nextBytes(iv);
        return iv;
    }

     static void IVinFile(byte[] iv, String file) { // запись вектора в файл
        try {
            Files.write(Paths.get(file + ".iv"), iv, StandardOpenOption.APPEND, StandardOpenOption.CREATE);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

     static byte[] IVfromFile(String file) { // чтение вектора из файла
        byte[] iv = new byte[BLOCKLENGTH];
        try {
            iv = Files.readAllBytes(Paths.get(file + ".iv"));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return iv;
    }
}
