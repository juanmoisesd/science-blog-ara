import random
import os
import datetime
import zipfile

def generate_arabic_text(word_count, topic):
    scientific_starters = [
        "تشير الدراسات الحديثة في مجال {topic} إلى أن ",
        "من وجهة نظر علمية، يعتبر {topic} من أهم المجالات التي ",
        "في هذا البحث، نقوم بتحليل تأثير المتغيرات المختلفة على ",
        "لقد أثبتت التجارب المعملية أن هناك علاقة طردية بين ",
        "على مر السنين، تطور فهمنا لـ {topic} بفضل التقدم التكنولوجي في ",
        "يهدف هذا التحليل المنهجي لـ {topic} إلى توضيح ",
        "من خلال مراجعة الأدبيات العلمية المتعلقة بـ {topic}، نجد أن ",
        "تلعب العوامل البيولوجية دوراً حاسماً في تطور {topic} خاصة عند ",
        "تساهم الأبحاث النوعية في تعميق معرفتنا بـ {topic} من خلال ",
        "إن الربط بين النظرية والتطبيق في {topic} يكشف عن "
    ]

    fillers = [
        "ومن الجدير بالذكر أن العمليات الحيوية تلعب دوراً محورياً في تحديد المسار السلوكي للفرد.",
        "كما أن التفاعل بين العوامل الوراثية والبيئية يساهم بشكل كبير في تشكيل ملامح الشخصية.",
        "وتؤكد النتائج التي تم التوصل إليها على أهمية الاستمرار في البحث العلمي الجاد والممنهج.",
        "إن التحليل الإحصائي للبيانات أظهر دلالات معنوية واضحة تدعم الفرضية الأساسية للدراسة.",
        "وفي هذا السياق، يجب أن نأخذ بعين الاعتبار القيود المنهجية التي قد تؤثر على تعميم النتائج.",
        "إن التكامل بين العلوم المختلفة يفتح آفاقاً جديدة لفهم الظواهر المعقدة في الطبيعة البشرية.",
        "وتشير الأدبيات السابقة إلى وجود تباين ملحوظ في الاستجابات العصبية تجاه المحفزات الخارجية.",
        "إن استخدام تقنيات التصوير بالرنين المغناطيسي الوظيفي قد مكننا من مراقبة نشاط الدماغ بدقة عالية.",
        "ويمكن القول إن الاستنتاجات الحالية تفتح الباب أمام استراتيجيات علاجية مبتكرة وفعالة.",
        "إن الالتزام بالمعايير الأخلاقية في البحث العلمي هو الركيزة الأساسية لضمان مصداقية النتائج.",
        "يبرز دور الإدراك في توجيه السلوكيات اليومية واتخاذ القرارات المعقدة.",
        "تعتبر البيئة المحيطة عاملاً حاسماً في تعزيز أو إعاقة الإمكانات الفطرية للفرد.",
        "أظهرت الدراسات الطولية أن التدخل المبكر يعزز النتائج الإيجابية في النمو النفسي.",
        "تمثل الذاكرة حجر الزاوية في بناء الهوية الشخصية والتعلم المستمر عبر الحياة.",
        "إن الفهم العميق للعمليات الذهنية يتطلب تعاوناً وثيقاً بين علم النفس وعلم الأعصاب.",
        "ساهمت النظريات الحديثة في تغيير جذري لنماذج التفكير التقليدية في هذا المجال.",
        "تشير الملاحظات الإكلينيكية إلى وجود ارتباط وثيق بين التوتر المزمن والقدرات المعرفية.",
        "يسعى هذا البحث لتسليط الضوء على الآليات النفسية الكامنة خلف الاستجابات السلوكية.",
        "إن المنهجية الصارمة تضمن الحصول على بيانات موثوقة يمكن تكرار نتائجها علمياً.",
        "تعتبر العلاقة بين الدماغ والسلوك من أكثر القضايا إثارة للجدل في العلم الحديث."
    ]

    text = ""
    current_word_count = 0

    while current_word_count < word_count:
        sentence = random.choice(scientific_starters).format(topic=topic) + random.choice(fillers) + " "
        text += sentence
        current_word_count += len(sentence.split())

        if current_word_count % 500 < 60:
            text += "\n\n<h3>تحليل إضافي لـ " + topic + "</h3>\n\n"

    return text

def create_wxr_item(category, index):
    categories_dict = {
        "psychology": ["علم النفس المعرفي", "السلوك البشري", "الصحة النفسية", "الذكاء العاطفي", "علم النفس التربوي", "الاضطرابات النفسية"],
        "neuroscience": ["الجهاز العصبي", "المرونة العصبية", "النواقل العصبية", "تشريح الدماغ", "الذاكرة والتعلم", "التدهور المعرفي"]
    }

    cat_arabic = "علم النفس" if category == "psychology" else "علوم الأعصاب"
    topic = random.choice(categories_dict[category])
    title = f"{topic} - دراسة معمقة رقم {index}"

    author_bio = """
<hr />
<h3>عن المؤلف</h3>
<p><strong>د. خوان مويسيس دي لا سيرنا</strong><br />
دكتور في علم النفس، ماجستير في علوم الأعصاب وبيولوجيا السلوك، أستاذ جامعي وناشر علمي.</p>
"""

    content = f"""
<h2>{title}</h2>

<h3>ملخص (Abstract)</h3>
<p>يتناول هذا البحث دراسة تفصيلية حول {topic}، حيث نسعى لاستكشاف الآليات الكامنة والتفاعلات المعقدة التي تؤثر على هذا المجال. تم استخدام منهجية علمية صارمة لضمان دقة النتائج وتوافقها مع المعايير العالمية.</p>

<h3>مقدمة (Introduction)</h3>
<p>{generate_arabic_text(600, topic)}</p>

<h3>المنهجية (Methodology)</h3>
<p>{generate_arabic_text(600, topic)}</p>

<h3>النتائج (Results)</h3>
<p>{generate_arabic_text(600, topic)}</p>

<h3>المناقشة (Discussion)</h3>
<p>{generate_arabic_text(600, topic)}</p>

<h3>الخاتمة (Conclusion)</h3>
<p>{generate_arabic_text(600, topic)}</p>

<h3>المراجع (Bibliography)</h3>
<ul>
<li>De la Serna, J. M. (2024). <em>Advanced Studies in {cat_arabic}</em>. International Scientific Press.</li>
<li>Smith, A., & Jones, B. (2023). <em>The Future of Human Behavior</em>. Science Today Journal.</li>
<li>Brown, L. (2025). <em>Neurological Patterns and Psychological Impacts</em>. Academic Insights.</li>
<li>Miller, R. (2022). <em>Cognitive Foundations</em>. Research Gate.</li>
<li>Wilson, K. (2021). <em>Experimental Methods in Science</em>. University Press.</li>
</ul>

{author_bio}
"""

    post_date = (datetime.datetime.now() - datetime.timedelta(days=index)).strftime("%Y-%m-%d %H:%M:%S")

    item = f"""
    <item>
        <title>{title}</title>
        <link>https://science-blog-ara.pages.dev/{category}/post-{index}</link>
        <pubDate>{post_date}</pubDate>
        <dc:creator><![CDATA[juanmoisesd]]></dc:creator>
        <guid isPermaLink="false">https://science-blog-ara.pages.dev/?p={index + (1000 if category == "neuroscience" else 0)}</guid>
        <description></description>
        <content:encoded><![CDATA[{content}]]></content:encoded>
        <excerpt:encoded><![CDATA[]]></excerpt:encoded>
        <wp:post_id>{index + (1000 if category == "neuroscience" else 0)}</wp:post_id>
        <wp:post_date>{post_date}</wp:post_date>
        <wp:post_date_gmt>{post_date}</wp:post_date_gmt>
        <wp:comment_status>open</wp:comment_status>
        <wp:ping_status>open</wp:ping_status>
        <wp:post_name>post-{category}-{index}</wp:post_name>
        <wp:status>publish</wp:status>
        <wp:post_parent>0</wp:post_parent>
        <wp:menu_order>0</wp:menu_order>
        <wp:post_type>post</wp:post_type>
        <wp:post_password></wp:post_password>
        <wp:is_sticky>0</wp:is_sticky>
        <category domain="category" slug="{category}"><![CDATA[{cat_arabic}]]></category>
    </item>
"""
    return item

def generate_wxr_file(filename, category, start_index, end_index):
    header = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:wp="http://wordpress.org/export/1.2/"
>
<channel>
    <title>المدونة العلمية - د. خوان مويسيس دي لا سيرنا</title>
    <link>https://science-blog-ara.pages.dev</link>
    <description>مدونة علمية متخصصة في علم النفس وعلوم الأعصاب</description>
    <pubDate>{datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>
    <language>ar</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:base_site_url>https://science-blog-ara.pages.dev</wp:base_site_url>
    <wp:base_blog_url>https://science-blog-ara.pages.dev</wp:base_blog_url>

    <wp:author>
        <wp:author_id>1</wp:author_id>
        <wp:author_login><![CDATA[juanmoisesd]]></wp:author_login>
        <wp:author_email><![CDATA[juanmoisesd@example.com]]></wp:author_email>
        <wp:author_display_name><![CDATA[د. خوان مويسيس دي لا سيرنا]]></wp:author_display_name>
        <wp:author_first_name><![CDATA[خوان مويسيس]]></wp:author_first_name>
        <wp:author_last_name><![CDATA[دي لا سيرنا]]></wp:author_last_name>
    </wp:author>

    <wp:category>
        <wp:term_id>1</wp:term_id>
        <wp:category_nicename><![CDATA[psychology]]></wp:category_nicename>
        <wp:category_parent><![CDATA[]]></wp:category_parent>
        <wp:cat_name><![CDATA[علم النفس]]></wp:cat_name>
    </wp:category>
    <wp:category>
        <wp:term_id>2</wp:term_id>
        <wp:category_nicename><![CDATA[neuroscience]]></wp:category_nicename>
        <wp:category_parent><![CDATA[]]></wp:category_parent>
        <wp:cat_name><![CDATA[علوم الأعصاب]]></wp:cat_name>
    </wp:category>
"""
    footer = """
</channel>
</rss>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header)
        for i in range(start_index, end_index + 1):
            f.write(create_wxr_item(category, i))
        f.write(footer)

def main():
    os.makedirs("exports", exist_ok=True)
    os.makedirs("public", exist_ok=True)

    print("Generating WordPress Import Package...")
    generate_wxr_file("exports/psychology_1.xml", "psychology", 1, 500)
    generate_wxr_file("exports/psychology_2.xml", "psychology", 501, 1000)
    generate_wxr_file("exports/neuroscience_1.xml", "neuroscience", 1, 500)
    generate_wxr_file("exports/neuroscience_2.xml", "neuroscience", 501, 1000)

    with zipfile.ZipFile("public/wordpress_import_package.zip", "w") as zipf:
        for f in ["psychology_1.xml", "psychology_2.xml", "neuroscience_1.xml", "neuroscience_2.xml"]:
            zipf.write(os.path.join("exports", f), f)
            print(f"Added {f} to zip")

    print("Done! Package created in public/wordpress_import_package.zip")

if __name__ == "__main__":
    main()
