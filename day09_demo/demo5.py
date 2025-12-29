import chromadb
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


embed_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)


raw_text = """Animation in Japan began in the early 20th century, when filmmakers started to experiment with techniques pioneered in France, Germany, the United States, and Russia.[22] A claim for the earliest Japanese animation is Katsudō Shashin (c. 1907),[23] a private work by an unknown creator.[24] In 1917, the first professional and publicly displayed works began to appear; animators such as Ōten Shimokawa, Seitarō Kitayama, and Jun'ichi Kōuchi (known as the "fathers of anime") produced numerous films, with the oldest surviving one being Kōuchi's Namakura Gatana.[25] Many early works were lost in the destruction of Shimokawa's warehouse during the 1923 Great Kantō earthquake.[26]

By the mid-1930s, animation was well-established in Japan as an alternative format to live action works. It suffered competition from foreign producers, such as Disney, and many animators, including Noburō Ōfuji and Yasuji Murata, continued to work with cheaper cutout animation rather than cel animation.[27] Other creators, including Kenzō Masaoka and Mitsuyo Seo, nevertheless made great strides in technique, benefiting from the patronage of the government, which employed animators to produce educational shorts and propaganda.[28] In 1940, the government dissolved several artists' organizations to form the Shin Nippon Mangaka Kyōkai.[b][29] The first talkie anime was Chikara to Onna no Yo no Naka (1933), a short film produced by Masaoka.[30][31] The first feature-length anime film was Momotaro: Sacred Sailors (1945), produced by Seo with a sponsorship from the Imperial Japanese Navy.[32] The 1950s saw a proliferation of short, animated advertisements created for television.[33]

Modern era

Frame from the opening sequence of Osamu Tezuka's 1963 TV series Astro Boy
In the 1960s, manga artist and animator Osamu Tezuka adapted and simplified Disney animation techniques to reduce costs and limit frame counts in his productions.[34] Originally intended as temporary measures to allow him to produce material on a tight schedule with inexperienced staff, many of his limited animation practices came to define the medium's style.[35] Three Tales (1960) was the first anime film broadcast on television;[36] the first anime television series was Instant History (1961–64).[37] An early and influential success was Astro Boy (1963–66), a television series directed by Tezuka based on his manga of the same name. Many animators at Tezuka's Mushi Production later established major anime studios, among those being Madhouse, Sunrise, and Studio Pierrot.

The 1970s saw growth in the popularity of manga, many of which later received animated adaptations. Tezuka's work—and that of other pioneers in the field—inspired characteristics and genres that remain fundamental elements of anime today. The giant robot genre (also known as "mecha"), for instance, took shape under Tezuka, developed into the super robot genre under Go Nagai and others, and was revolutionized at the end of the decade by Yoshiyuki Tomino, who developed the real robot genre.[38] Robot anime series such as Gundam, Space Runaway Ideon,[39] and Super Dimension Fortress Macross were influential classics in the 1980s, and the genre remained one of the most popular in the following decades.[40] The bubble economy of the 1980s spurred a new era of high-budget and experimental anime films, including Nausicaä of the Valley of the Wind (1984), Royal Space Force: The Wings of Honnêamise (1987), and Akira (1988).[41]

Experimental anime titles continued to draw a
The anime industry consists of over 430 production companies, including major studios such as Studio Ghibli, Kyoto Animation, Sunrise, Bones, Ufotable, MAPPA, Wit Studio, CoMix Wave Films, Madhouse, Inc., TMS Entertainment, Studio Pierrot, Production I.G, Nippon Animation and Toei Animation. Since the 1980s, the medium has also seen widespread international success with the rise of foreign dubbed and subtitled programming, and since the 2010s due to the rise of streaming services and a widening demographic embrace of anime culture, both within Japan and worldwide.[5][6] As of 2016, Japanese animation accounted for 60% of the world's animated television shows.[7] By 2022, anime had become one of the fastest-growing genres of content globally.[8] The medium is currently characterised by increased globalisation, expansive cross-cultural collaboration, and significant brand integration, as Japanese-produced animation continues to influence and shape media and popular culture on a global scale.[9]
   In English, anime—when used as a common noun—normally functions as a mass noun. (For example: "Do you watch anime?" or "How much anime have you watched?")[17][18] As with a few other Japanese words, such as saké and Pokémon, English texts sometimes spell anime as animé (as in French), with an acute accent over the final e, to cue the reader to pronounce the letter, not to leave it silent as English orthography may suggest. Prior to the widespread use of anime, the term Japanimation, a portmanteau of Japan and animation, was prevalent throughout the 1970s and 1980s. In the mid-1980s, the term anime began to supplant Japanimation;[19] in general, the latter term now only appears in period works where it is used to distinguish and identify Japanese animation.[2],In English, anime—when used as a common noun—normally functions as a mass noun. (For example: "Do you watch anime?" or "How much anime have you watched?")[17][18] As with a few other Japanese words, such as saké and Pokémon, English texts sometimes spell anime as animé (as in French), with an acute accent over the final e, to cue the reader to pronounce the letter, not to leave it silent as English orthography may suggest. Prior to the widespread use of anime, the term Japanimation, a portmanteau of Japan and animation, was prevalent throughout the 1970s and 1980s. In the mid-1980s, the term anime began to supplant Japanimation;[19] in general, the latter term now only appears in period works where it is used to distinguish and identify Japanese animation.[2]"""


chunks = text_splitter.split_text(raw_text)


embeddings = embed_model.embed_documents(chunks)


client = chromadb.PersistentClient(path="./chroma-db")
collection = client.get_or_create_collection(name="demo")

ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
metadatas = [{"source": "example.py"} for _ in range(len(chunks))]

collection.add(
    ids=ids,
    embeddings=embeddings,
    documents=chunks,
    metadatas=metadatas
)

print("✅ Documents stored in ChromaDB")


query = " anime "
query_embedding = embed_model.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


print("\n🔍 Search Results:\n")

for i, (doc, meta, dist) in enumerate(
    zip(results["documents"][0], results["metadatas"][0], results["distances"][0]),
    start=1
):
    print(f"Result {i}:")
    print(f"Text: {doc}")
    print(f"Metadata: {meta}")

    print("-" * 50)
