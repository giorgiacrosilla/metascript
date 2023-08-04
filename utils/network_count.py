import xml.etree.ElementTree as ET
from collections import defaultdict
import csv

# Your XML content as a string
xml_content = """

    <body>
      <div type="chapter" n="1">
        <head>1.</head>
        <p>
          <quote>"TWENTY-FOUR brown-skinned slaves rowed the splendid gallery which was to bring
          Prince Amgiad to the palace of the caliph. The Prince, wrapped in his purple cloak, lay
          alone on the deck
            under the dark-blue, starry sky, and his gaze—"</quote><lb /> So far the <rs
            ref="#daughter">little girl</rs> had read aloud.Then, suddenly, her eyelids drooped. Her
          parents looked at each other and smiled. <rs type="character" ref="#Fridolin">Fridolin</rs>
          bent down, kissed her blond hair and closed the book which was lying on the untidy table.
          The child looked up as if caught at some mischief.<lb />
            <said aloud="true" direct="true"
            who="Fridolin" listener="daughter">"It's nine o'clock,"</said> her father said, <said
            aloud="true" direct="true" who="Fridolin" listener="daughter">"and time you were in
            bed."</said> <rs
            ref="#Albertina">Albertina</rs>also bent over her, and as her hand met her husband's on
          the beloved forehead, they looked at each other with a tender smile not meant for the
          child. The <rs ref="#governess">governess</rs> entered and asked the little girl to say
          good-night. She got up obediently, kissed her father and mother and walked out quietly
          hand in hand with the young woman. <rs
            ref="#Fridolin">Fridolin</rs> and <rs type="character" ref="#Albertina">
            Albertina</rs>, left alone under the reddish glow of the hanging-lamp, continued the
          conversation they had begun before supper. </p>

        <p> It dealt with their experiences the night before at the <eventName ref="#MASQ">masquerade
          ball</eventName>. They had decided to attend it just before the end of the <eventName
            ref="#CARNIVAL">carnival period</eventName>, as their first one of the season. No sooner
          had <rs type="character" ref="Fridolin">Fridolin</rs> entered the ball-room than he was
          greeted, like a long lost friend, by <rs type="character" ref="#TWOW">two
            women</rs> in red dominoes. <rs type="character" ref="#Fridolin">He</rs> had no idea who
          they were, although they were unusually well-informed about many affairs of his student
          days and internship. They had invited him into a box with great friendliness, but had left
          again with the promise that they would soon return without masks. When they did not
          appear, he became impatient and went down to the ball-room floor hoping to meet them
          again, but eagerly as he scanned the room, he could not see them anywhere. Instead,
          however, another woman unexpectedly took his arm. It was his <rs type="character"
            ref="#Albertina">wife</rs>. She had just freed herself from the company of a <rs
            type="character"
            ref="#STRANGER">stranger</rs> whose blase manner and apparently Polish accent had at
          first charmed her. Suddenly he had offended her--frightened her by a rather common and
          impertinent remark. <rs type="character" ref="#Fridolin">Fridolin</rs> and <rs
            ref="#Albertina">Albertina</rs> were glad to have escaped from a disappointingly
          commonplace masquerade prank, and soon sat like two lovers, among the other couples, in
          the buffet, eating oysters and drinking champagne. They chatted gaily, as though they had
          just made each other's acquaintance, acting a comedy of courting, bashful resistance,
          seduction and surrender. After driving home quickly through the snowy winter night, they
          sank into each other's arms and were more blissful in their ardent love than they had been
          for a long time. The gray of morning awakened them only too soon. Fridolin's profession
          summoned him to his patients at an early hour, while <rs type="character" ref="#Albertina">
          Albertina</rs> would not stay in bed longer because of her duties as housewife and mother.
          So the ensuing hours passed, soberly and predetermined, in daily routine and work, and the
          events of the night before, both those at the beginning and at the end, had faded. </p>

        <p>
          But now that the day's work was done— the child had gone to bed and no disturbance was
          likely—the shadowy forms of the masquerade, the melancholy stranger and the red dominoes,
          rose again into reality. And all at once those insignificant events were imbued, magically
          and painfully, with the deceptive glow of neglected opportunities. Harmless but probing
          questions, and sly, ambiguous answers were exchanged. Neither failed to notice
          that the other was not absolutely honest, and so they became slightly vindictive. They
          exaggerated the degree of attraction that their unknown partners at the ball had exerted
          upon them while each made fun of the other's tendencies to jealousy and denied his own.
          Soon, their light conversation about the trifling matters of the night before changed into
          a more serious discussion of those hidden, scarcely suspected wishes, which can produce
          dangerous whirlpools even in the serenest and purest soul. They spoke of those mysterious
          regions of which they were hardly conscious but toward which the incomprehensible wind of
          fate might some day drive them, even if only in their dreams. For though they were united
          in thought and feeling, they knew that the preceding day had not been the first time that
          the spirit of adventure, freedom and danger had beckoned them. Uneasy, and tormenting
          themselves, each sought with disingenuous curiosity to draw out confessions from the
          other. Anxiously, they searched within themselves for some indifferent fact, or trifling
          experience, which might express the inexpressible, and the honest confession of which
          might relieve them of the strain and the suspicion which were becoming unbearable. </p>

        <p> Whether <rs type="character" ref="#Albertina">Albertina</rs> was more impatient, more
          honest or more kind-hearted of the two, it was she who first summoned the courage for a
          frank confession. She asked <rs type="character" ref="#Fridolin">Fridolin</rs> in a rather
          uncertain voice whether he remembered the young man who—last summer at the seashore in
          Denmark—had been sitting one evening with two other officers at an adjoining table. He had
          received a telegram during dinner, whereupon he had hastily said "good-bye" to his
          friends.</p>
        <p>
          <rs type="character" ref="#Fridolin">Fridolin</rs> nodded. <said aloud="true"
            direct="true"
            who="Fridolin" listener="Albertina">"What
            about him?"</said> he asked. </p>
        <p>
          <said aloud="true" direct="true" who="Albertina" listener="Fridolin">I'd already seen him
          in the morning,"</said> she replied, <said aloud="true" direct="true" who="Albertina"
            listener="Fridolin">"as he was hurrying up the stairs in the hotel with
            his yellow hand-bag. He looked at me as he passed, but didn't stop until he had gone a
          few more steps.
            Then he turned and our eyes met. He didn't smile; in fact, it seemed to me that he
          scowled. I suppose I
            did the same, for I was very much stirred. That whole day I lay on the beach, lost in
          dreams. Had he
            called me—I thought—I could not have resisted. I thought I was ready for anything. I had
          practically
            resolved to give up you, the child, my future, and at the same time —if you can
          understand it?—you
            were dearer to me than ever. That same afternoon—surely you remember—we discussed many
          things
            very intimately, among others our common future, and our child. At sunset you and I were
          sitting on the
            balcony, when, down below on the beach, he passed without looking up. I was extremely
          thrilled to see
            him, but I stroked your forehead and kissed your hair, and my love for you was both
          sorrowful and
            compassionate. That evening at dinner I wore a white rose and you yourself said I was
          very beautiful.
            Perhaps it wasn't mere chance that the stranger and his friends sat near us. He didn't
          look at me, but I
            considered getting up, walking over to him and saying: Here I am, my beloved for whom I
          have waited —
            take me. At that moment the telegram was handed to him. He read it, turned pale,
          whispered a few
            words to the younger of the two officers—and glancing at me mysteriously he left the
          room."</said>
        </p>

        <p>
          <said aloud="true" direct="true" who="Fridolin" listener="Albertina">"And then?"</said>
          <rs
            ref="#Fridolin">Fridolin</rs> asked dryly when she stopped. </p>
        <p>
          <said aloud="true" direct="true" who="Albertina" listener="Fridolin">"That is all. I
            remember that I woke the next morning with a restless anxiety. I don't know whether I
            was afraid that he had left or that he might still be there. But when he didn't appear
            at noon, I breathed a sigh of relief. Don't ask any more, <rs ref="#Fridolin">Fridolin</rs>.
            I've told you the whole truth. And you, too, had some sort of experience at the
            seashore—I know it."</said>
        </p>

        <p>
          <rs ref="#Fridolin">Fridolin</rs> rose, walked up and down the room several times and then
          said: <said aloud="true" direct="true" who="Fridolin" listener="Albertina">"You're right."</said>
          He was standing at the window, his face in shadow and in a hoarse and slightly hostile
          voice he began: <said aloud="true" direct="true" who="Fridolin" listener="Albertina">In
          the morning, sometimes very early before you got up, I used to stroll along the beach, out
          beyond the town. Even at that hour the sun was always shining over the sea, bright and
          strong. Out there on the beach, as you know, were cottages, each one standing like a world
          in itself. Some had fenced-in gardens, others were surrounded only by the woods. The
          bathing-huts were separated from the cottages by the road and part of the beach. I hardly
          ever met people at such an early hour, and bathers were never out. One morning, quite
          suddenly, I noticed the figure of a woman. She had suddenly appeared on the narrow ledge
          of a bathing-hut, which rested on piles driven into the sand. She was cautiously
          advancing, placing one foot before the other, her arms extended backward against the
          wooden boards. She was quite a <rs ref="#younggirl">young girl</rs>, possibly fifteen
          years old, with loose blond hair hanging over her shoulders and on one side over her
          delicate breast. She was looking down into the water and was slowly moving along the wall,
          her gaze lowered in the direction of the far corner. All at once she stopped opposite me
          and reached far back with her arms as though trying to secure a firmer hold. Looking up,
          she suddenly saw me. A tremor passed through her body, as though she wished to drop into
          the water or run. But as she could move only very slowly on the narrow ledge, she had to
          stay where she was. She stood there with a face expressing at first fright, then anger,
          and finally embarrassment. All at once, however, she smiled, smiled marvelously. Her eyes
          welcomed me, beckoned to me, and at the same time slightly mocked me, as she glanced at
          the strip of water between us. Then she stretched her young and slender body, glad of her
          beauty, and proudly and sweetly stirred by my obvious admiration. We stood facing each
          other for perhaps ten seconds, with half-open lips and dazzled eyes. Involuntarily I
          stretched out my arms to her; her eyes expressed surrender and joy. Then she shook her
          head vigorously, took one arm from the wall and commanded me with a gesture to go away.
          When I didn't at once obey, her childlike eyes turned on me such a beseeching look that
          there was nothing for me to do but to go, and I went as quickly as possible. I did not
          look back once—not because I felt considerate, obedient or chivalrous, but because in her
          last glance I sensed an emotion so intense, so far beyond anything I had ever experienced,
          that I was not far from fainting."</said> And he stopped. </p>
        <p> With her eyes cast down and in a monotonous voice, <rs ref="#Albertina">
            Albertina</rs> asked: <said aloud="true" direct="true" who="Albertina"
            listener="Fridolin">And
            how often
            did you
            see her
            after that?"</said>
        </p>
        <p>
          <said aloud="true" direct="true" who="Fridolin" listener="Albertina">"What I have told
          you,"</said> <rs ref="#Fridolin">Fridolin</rs> answered, <said aloud="true" direct="true"
            who="Fridolin" listener="Albertina">"happened on the last day of our stay in Denmark.
          Otherwise I don't know what might have taken place. You, too, mustn't ask any more, <rs
              ref="#Albertina">Albertina</rs>."</said>
        </p>
        <p> He was still standing at the window, motionless as <rs
            ref="#Albertina">Albertina</rs> arose and walked over to him. There were tears in her
          eyes and a slight frown on her face. <said aloud="true" direct="true" who="Albertina"
            listener="Fridolin">"In the future let's always tell each other such
            things at once,"</said> she said. </p>
        <p>He nodded in silence. <said aloud="true" direct="true" who="Albertina"
            listener="Fridolin">"Will you promise me?"</said>
        </p>
        <p> He took her into his arms. <said aloud="true" direct="true" who="Fridolin"
            listener="Albertina">"Don't
            you know that?"</said> he asked. But his voice was still harsh. </p>
        <p>She took his hands and looked up at him with misty eyes, in the depths of which he could
          read her thoughts. She was thinking of his other and more real experiences, those of his
          young manhood, many of which she knew about. When they were first married he had yielded,
          all too readily, to her jealous curiosity and had told her (indeed it often seemed to him)
          had surrendered to her many secrets which he should rather have kept to himself. He knew
          that she was inevitably reminded of these affairs and he was hardly surprised when she
          murmured the half-forgotten name of one of his early sweethearts. It sounded to him a
          little like a reproach, or was it a covert threat?
        </p>
        <p> He raised her hands to his lips. <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"You may believe me, even
          though it sounds trite, that in every woman I thought I loved it was always you I was
          looking for—I know that better than you can understand it, <rs ref="#Albertina">Albertina</rs>
          ." </said>
        </p>
        <p>A dispirited smile passed over her face. <said aloud="true" direct="true"
            who="Albertina" listener="Fridolin">"And suppose before meeting you, I, too, had gone on
          a search for a
            mate?"</said> she asked. The look in her eyes changed, becoming cool and impenetrable,
          and he allowed her hands to slip from his, as though he had caught her lying or committing
          a breach of faith. She, however, continued: <said aloud="true" direct="true"
            who="Albertina" listener="Fridolin">"Oh, if you men knew!"</said> and again was silent. <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"If we
            knew—? What do you mean by that?"</said> In a strangely harsh voice she replied: <said
            aloud="true" direct="true" who="Albertina" listener="Fridolin">"About what you imagine,
          my dear."</said> <said aloud="true" direct="true" who="Fridolin" listener="Albertina">"<rs
              ref="#Albertina">Albertina</rs>!—then there is something that you've kept from me?"</said>
          She nodded, and looked down with a strange smile. Incomprehensible, monstrous doubts
          crossed his mind. <said aloud="true" direct="true" who="Fridolin" listener="Albertina">"I
          don't quite understand,"</said> he said. <said aloud="true" direct="true" who="Fridolin"
            listener="Albertina">"You were barely seventeen when we became engaged."</said><said
            aloud="true" direct="true" who="Albertina" listener="Fridolin">"Past sixteen, yes, <rs
              ref="#Fridolin">Fridolin</rs>. But it wasn't my fault that I was a virgin when I
          became your wife."</said> She looked at him brightly. <said aloud="true" direct="true"
            who="Fridolin" listener="Albertina">"<rs ref="#Albertina">Albertina</rs>——!"</said> But
          she continued: <said aloud="true" direct="true" who="Albertina" listener="Fridolin">"It
            was a beautiful summer evening at Lake Worther, just before our engagement, and a very
          handsome young man stood before my window that overlooked a large and spacious meadow. As
          we talked I thought to myself—just listen to this—what a charming young man that is—he
          would only have to say the word—it would have to be the right one, certainly—and I would
            go out with him into the meadow or the woods—or it would be even more beautiful in a
            boat
            on the lake—and I would grant him this night anything he might desire. That is what I
          thought to myself.—But he didn't say a word, that charming young man. He only kissed my
          hand tenderly— and next morning he asked me—if I would be his wife. And I said yes."</said>
        </p>
        <p>
          <rs
            ref="#Fridolin">Fridolin</rs> was annoyed and dropped her hand. <said aloud="true"
            direct="true" who="Fridolin" listener="Albertina">"And if,"</said> he said, <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"someone else had stood
            by your window that night and the right word had occurred to him, if it had been, for
          instance—"</said> He was considering, but she raised her hand protestingly. </p>
        <p><said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"Any other man—no
            matter who—could have said anything he liked—it would have been useless. And if it
            hadn't
            been you standing by the window, then very likely the summer evening wouldn't have been
          so
            beautiful."</said> And she smiled at him. </p>
        <p> There was a scornful expression about his mouth. <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"Yes,
            that's what you say now. Perhaps you even believe it at this moment. But——"</said>
        </p>
        <p>There was a knock on the door. The maid entered and said that the housekeeper from
          Schreyvogel Strasse had come to fetch the doctor, as the Privy Councilor was very low
          again. <rs
            ref="#Fridolin">
            Fridolin</rs> went out into the hall, and when the woman told him that the Councilor had
          had a very serious heart attack, he promised to come at once. As he was leaving, <rs
            ref="#Albertina">Albertina</rs> asked: <said
            aloud="true" direct="true" who="Albertina" listener="Fridolin">"You're going away?"</said>
          She said it with as much annoyance as if he were deliberately doing her an injustice. <rs
            ref="#Fridolin">Fridolin</rs> replied, with astonishment: <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"I suppose I've got to."</said>
          She sighed regretfully. <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"I hope it
            won't be very serious,"</said> said <rs
            ref="#Fridolin">Fridolin</rs>. <said
            aloud="true" direct="true" who="Fridolin" listener="Albertina">"Up to now three
          centigrams
            of morphine have always
            pulled him through."</said> The maid brought his fur coat, and absent-mindedly kissing <rs
            ref="#Albertina">Albertina</rs> on her forehead and mouth, as if everything during the
          last hour had been completely forgotten, he hurried away. </p>
      </div>
      <div type="chapter" n="2">
        <head>2.</head>
        <p>WHEN <rs ref="#Fridolin">
            Fridolin</rs> reached the street, he unbuttoned his coat. It had suddenly begun to thaw;
          the snow on the sidewalk was almost gone, and there was a touch of spring in the air. It
          was less than a quarter of an hour's walk to Schreyvogel Strasse from his home near the
          General Hospital, and he soon reached the old house. He walked up the dimly lighted
          winding staircase to the second floor and pulled the bell-rope. But before the
          old-fashioned bell was heard, he noticed that the door was ajar, and entering through the
          unlighted foyer into the living room he saw at once that he had come too late. The
          green-shaded kerosene lamp which was hanging from the low ceiling cast a dim light on the
          bedspread under which a lean body lay motionless. <rs ref="#Fridolin">Fridolin</rs> knew
          the old man so well that he seemed to see the face plainly, although it was outside the
          circle of light— the high forehead, the thin and lined cheeks, the snow-white beard and
          also the strikingly ugly ears with coarse, white hairs. At the foot of the bed sat <rs
            ref="#Marianne">Marianne</rs>, the Councilor's daughter, completely exhausted, her arms
          hanging limply from her shoulders. An odor of old furniture, medicine, petroleum and
          cooking pervaded the room, and in addition to that there was a trace of eau de Cologne and
          scented soap. <rs
            ref="#Fridolin">Fridolin</rs> also noticed the indefinite, sweetish scent of this pale
          girl who was still young and who had been slowly fading for months and years under the
          stress of severe household duties, nursing and night watches. When the doctor entered she
          looked up, but because of the dim light he could not see whether she had blushed, as
          usual, when he appeared. She started to rise, but he stopped her with a movement of his
          hand, and so she merely greeted him with a nod, her eyes large and sad. He stepped to the
          head of the bed and mechanically placed his hands on the forehead of the dead man and on
          the arms which were lying on the bed-spread in loose and open shirt sleeves. His shoulders
          drooped with a slight expression of regret. He stuck his hands into the pockets of his
          coat and his eyes wandered about the room until they finally rested on <rs ref="#Marianne">
          Marianne</rs>. Her hair was blond and thick, but dry; her neck well-formed and slender,
          although a little wrinkled and rather yellow; and her lips were thin and firmly pressed
          together. <said aloud="true" direct="true" who="Fridolin" listener="Marianne">Well, my
          dear <rs ref="#Marianne">Marianne</rs>,"</said> he said in a slightly embarrassed whisper, <said
            aloud="true" direct="true" who="Fridolin" listener="Marianne">"you weren't entirely
          unprepared for
            this."</said> She held out her hand to him. He took it sympathetically and inquired
          about the particulars of the final, fatal attack. <said aloud="true" direct="false"
            who="Marianne" listener="Fridolin">She reported briefly and to the point, and then spoke
          of her father's last comparatively easy days, during which <rs ref="#Fridolin">
              Fridolin</rs> had not seen him.</said> Drawing up a chair, he sat down opposite her,
          and tried to console her by <said aloud="true" direct="false" who="Fridolin"
            listener="Marianne">saying that her father must have suffered very little at the last.
            He then
            asked if any of her relatives had been notified.</said> <said aloud="true" direct="false"
            who="Marianne" listener="Fridolin">Yes, she said, the housekeeper had
            already gone to tell her uncle, and very likely Doctor Roediger would soon appear.</said> <said
            aloud="true" direct="true" who="Marianne" listener="Fridolin">"My
            fiance,"</said> she added, and did not look him straight in the eye. <rs ref="#Fridolin">
          Fridolin</rs> simply nodded. During the year he had met <rs ref="#Roediger">Doctor
            Roediger</rs> two or three times in the Councilor's house. The pale young man—an
          instructor in History at the University of Vienna—was of an unusually slender build with a
          short, blond beard and spectacles, and had made quite a good impression upon him, without,
          however, arousing his interest beyond that. <rs ref="#Marianne">Marianne</rs> would
          certainly look better, he thought to himself, if she were his mistress. Her hair would be
          less dry, her lips would be fuller and redder. <said aloud="false" direct="false"
            who="Fridolin">I wonder how
            old she is, he reflected. The first time I attended the Councilor, three or four years
          ago, she was twentv-three. At that time her mother was still living and she was more
          cheerful than now. She even took singing lessons for a while. So she is going to marry
            this instructor! I wonder why? She surely isn't in love with him, and he isn't likely to
          have much money either. What kind of a marriage will it turn out to be? Probably like a
          thousand others. But it's none of my business. It's quite possible that I shall never see
          her again, since there's nothing more for me to do here. Well, many others that I cared
            for have gone the same way.</said> As these thoughts passed through his mind, <rs
            ref="#Marianne">Marianne</rs> began to speak of her father—with fervor—as if his death
          had suddenly made him a more remarkable person. <said aloud="false" direct="false"
            who="Fridolin">Then he was really only fifty-four years old? Well, of course, he had had
          so many worries and disappointments—his wife always ill—and his son such a grief! What,
            she had a brother? Certainly, she had once told the doctor about him. </said>Her brother
          was now living somewhere abroad. A picture that he had painted when he was fifteen was
          hanging over there in <rs ref="#Marianne">Marianne</rs>'s room. It represented an officer
          galloping down a hill. Her father had always pretended not to see it although it wasn't
          bad. Oh yes, if he'd had a chance her brother might have made something of himself. <said
            aloud="false" direct="false"
            who="Fridolin">How
            excitedly she speaks</said>, <rs ref="#Fridolin">
            Fridolin</rs> thought, <said aloud="false" direct="false"
            who="Fridolin">and how bright her eyes are! Is it fever? Quite possibly. She's
            grown much thinner. Probably has tuberculosis.</said> She kept up her stream of talk,
          but it seemed to him that she didn't quite know what she was saying. It was twelve years
          since her brother had left home. In fact, she had been a child when he disappeared. They
          had last heard from him four or five years ago, at Christmas, from a small city in Italy.
          Strange to say, she had forgotten the name. She continued like this for a while, almost
          incoherently. Suddenly she stopped and sat there silently, her head resting in her hands. <rs
            ref="#Fridolin">Fridolin</rs> was tired and even more bored. He was anxiously waiting
          for some one to come, her relatives, or her fiance. The silence in the room was
          oppressive. It seemed to him that the dead man joined in the silence, deliberately and
          with malicious joy. With a side glance at the corpse, he said: <said aloud="true"
            direct="true" who="Fridolin" listener="Marianne">At any rate, Fraulein <rs
              ref="#Marianne">Marianne</rs>, as things are now, it is fortunate that you won't have
          to stay in this house very much longer."</said> And when she raised her head a little,
          without, however, looking at <rs
            ref="#Fridolin">Fridolin</rs>, he continued: <said aloud="true" direct="true"
            who="Fridolin" listener="Marianne">"I suppose your fiance will soon get a
            professorship. The chances for promotion are more favorable in the Faculty of Philosophy
          than with us in Medicine."</said> He was thinking that, years ago, he also had aspired to
          an academic career, but because he wanted a comfortable income, he had finally decided to
          practice medicine. Suddenly he felt that compared with this noble <rs ref="#Roediger">Doctor
          Roediger</rs>, he was the inferior. <said aloud="true" direct="true" who="Marianne"
            listener="Fridolin">We shall move soon,"</said> <rs ref="#Marianne">Marianne</rs>
          listlessly, <said aloud="true" direct="true" who="Marianne" listener="Fridolin">"he has a
          post at the University of Gottingen."</said> <said aloud="true" direct="true"
            who="Fridolin" listener="Marianne">"Oh,"</said> said <rs ref="#Fridolin">Fridolin</rs>,
          and was about to congratulate her but it seemed rather out of place at the moment. He
          glanced at the closed window, and without asking for permission but availing himself of
          his privilege as a doctor, he opened both casements and let some air in. It had become
          even warmer and more spring-like, and the breeze seemed to bring with it a slight
          fragrance of the distant awakening woods. When he turned back into the room, he saw <rs
            ref="#Marianne">Marianne</rs>'s eyes fixed upon him with a questioning look. He moved
          nearer to her and said: <said aloud="true" direct="true" who="Fridolin"
            listener="Marianne">"I hope the fresh air will be good for you. It has become quite
            warm, and last night"</said>—he was about to say: we drove home from the masquerade in a
          snowstorm, but he quickly changed the sentence and continued: <said aloud="true"
            direct="true" who="Fridolin" listener="Marianne">"Last night the snow was
            still lying on the streets a foot and a half deep."</said> She hardly heard what he
          said. Her eyes became moist, large tears streamed down her cheeks and again she buried her
          face in her hands. In spite of himself, he placed his hand on her head, caressing it. He
          could feel her body beginning to tremble, and her sobs which were at first very quiet,
          gradually became louder and finally quite unrestrained. All at once she slipped down from
          her chair and lay at <rs ref="#Fridolin">Fridolin</rs>'s feet, clasping his knees with her
          arms and pressing her face against them. Then she looked up to him with large eyes, wild
          with grief, and whispered ardently: <said aloud="true" direct="true" who="Marianne"
            listener="Fridolin">"I don't want to leave here. Even if you never return, if I
            am never to see you again, I want, at least, to live near you."</said> He was touched
          rather than surprised, for he had always known that she either was, or imagined herself to
          be, in love with him. <said aloud="true" direct="true" who="Fridolin" listener="Marianne">"Please—get
          up, <rs ref="#Marianne">Marianne</rs>,"</said> he said softly and bending down he gently
          raised her. Of course, she is hysterical, he remarked to himself and he glanced at her
          dead father. <said aloud="false" direct="false" who="Fridolin">I wonder if he hears
          everything</said>, he thought. Perhaps he isn't really dead. Perhaps everyone in the first
          hours after passing away, is only in a coma. He put his arms about her in a very
          hesitating embrace, and almost against his will he kissed her on the forehead, an act that
          somehow seemed rather ridiculous. He had a fleeting recollection of reading a novel years
          ago in which a young man, still almost a boy, had been seduced, in fact, practically
          raped, by the friend of his mother at the latter's deathbed. At the same time he thought
          of his wife, without knowing why, and he was conscious of some bitterness and a vague
          animosity against the man with the yellow hand-bag on the hotel stairs in Denmark. He held <rs
            ref="#Marianne">Marianne</rs> closer, but without the slightest emotion. The sight of
          her lustreless, dry hair, the indefinite, sweetish scent of her unaired dress gave him a
          slight feeling of revulsion. The bell outside rang again, and feeling he was released, he
          hastily kissed <rs ref="#Marianne">
            Marianne</rs>'s hand, as if in gratitude, and went to open the door. <rs ref="#Roediger">Doctor
          Roediger</rs> stood there, in a dark gray top-coat, an umbrella in his hand and a serious
          face, appropriate to the occasion. The two men greeted each other much more cordially than
          was called for by their actual state of acquaintance. Then they stepped into the room.
          After an embarrassed look at the deceased, <rs ref="#Roediger">Roediger</rs> expressed his
          sympathy to <rs
            ref="#Marianne">Marianne</rs>, while <rs ref="#Fridolin">Fridolin</rs> went into the
          adjoining room to write out the official death certificate. He turned up the gas-light
          over the desk and his eyes fell upon the picture of the whiteuniformed officer, galloping
          down hill, with drawn sabre, to meet an invisible enemy. It hung in a narrow frame of dull
          gold and rather resembled a modest chromo-lithograph. With his death-certificate filled
          out, <rs
            ref="#Fridolin">Fridolin</rs> returned to the room where the engaged couple sat, hand in
          hand, by the bed of the dead Councilor. Again the door-bell rang and Doctor Roediger rose
          to answer it. While he was gone, <rs ref="#Marianne">Marianne</rs>, with her eyes on the
          floor, said, almost inaudibly: <said aloud="true" direct="true" who="Marianne"
            listener="Fridolin">"I love you,"</said>and <rs ref="#Fridolin">Fridolin</rs> answered
          by <said aloud="true" direct="false" who="Fridolin" listener="Marianne">pronouncing her
          name tenderly</said>. Then <rs ref="#Roediger">Roediger</rs> came back with an elderly
          couple, <rs
            ref="#Marianne">Marianne</rs>'s uncle and aunt, and a few words, appropriate to the
          occasion, were exchanged, with the usual embarrassment in the presence of one who has just
          died. The little room suddenly seemed crowded with mourners. <rs
            ref="#Fridolin">Fridolin</rs> felt superfluous, took his leave and was escorted to the
          door by Roediger who said a few words of gratitude and expressed the hope of seeing him
          soon again. </p>
      </div>
      <div type="chapter" n="3">
        <head>3.</head>
        <p>WHEN <rs ref="#Fridolin">Fridolin</rs> stood on the street in front of the house, he
          looked up at the window which he himself had opened a little while before. The casements
          were swaying slightly in the wind of early spring, and the people who remained behind them
          up there, the living as well as the dead, all seemed unreal and phantomlike. He felt as if
          he had escaped from something, not so much from an adventure, but rather from a melancholy
          spell the power of which he was trying to break. He felt strangely disinclined to go home.
          The snow in the streets had melted, except where little heaps of dirty white had been
          piled up on either side of the curb. The gas-flame in the street lamps flickered and a
          nearby church bell struck eleven. <rs ref="#Fridolin">
            Fridolin</rs> decided that before going to bed, he would spend a half hour in a quiet
          nook of a cafe near his residence. As he walked through Rathaus Park he noticed here and
          there on benches standing in the shadow, that couples were sitting, clasped together, just
          as if Spring had actually arrived and no danger were lurking in the deceptive, warm air. A
          tramp in tattered clothes was lying full length on a bench with his hat over his face. <said
            aloud="false" direct="false" who="Fridolin">Suppose I wake him and give him some money
          for a night's lodging </said>, <rs ref="#Fridolin">
            Fridolin</rs> thought. <said
            aloud="false" direct="false" who="Fridolin">But what good would that do? Then I would
          have to provide for the
            next night, too, or there'd be no sense in it, and in the end I might be suspected of
          having criminal relations with him.</said> He quickened his steps to escape as rapidly as
          possible from all responsibility and temptation. <said
            aloud="false" direct="false" who="Fridolin">And why only this one?</said> he asked
          himself. There are thousands of such poor devils in Vienna alone. It's manifestly
          impossible to help all of them or to worry about all the poor wretches! He was reminded of
          the dead man he had just left, and shuddered; in fact, he felt slightly nauseated at the
          thought that decay and decomposition, according to eternal laws, had already begun their
          work in the lean body under the brown flannel blanket. He was glad that he was still
          alive, and in all probability these ugly things were still far removed from him. He was,
          in fact, still in the prime of youth, he had a charming and lovable wife and could have
          several women in addition, if he happened to want them, although, to be sure, such affairs
          required more leisure than was his. He then remembered that he would have to be in his
          ward at the hospital at eight in the morning, visit his private patients from eleven to
          one, keep office hours from three to five, and that even in the evening he had several
          appointments to visit patients. Well, he hoped that it would be some time before he would
          again be called out so late at night. As he crossed Rathaus Square, which had a dull gleam
          like a brownish pond, and turned homeward, he heard the muffled sound of marching steps in
          the distance. Then he saw, still quite far away, a small group of fraternity students, six
          or eight in number, turning a corner and coming towards him. When the light of a street
          lamp fell upon them he thought he recognized them, with their blue caps, as members of the
          Alemannia, for although he had never belonged to a fraternity, he had fought a few sabre
          duels in his time. In thinking of his student days he was reminded again of the <rs
            ref="#TWOW">red
            dominoes</rs> who had lured him into a box at the ball the night before and then had so
          shamefully deserted him. The students were quite near now; they were laughing and talking
          loudly. Perhaps one or two of them were from the hospital? But it was impossible to see
          their faces plainly because of the dim light, and he had to stay quite close to the houses
          so as not to collide with them. Now they had passed. Only the one in the rear, a tall
          fellow with open overcoat and a bandage over his left eye, seemed to lag behind, and
          deliberately bumped into him with his raised elbow. It couldn't have been mere chance. <said
            aloud="false" direct="false" who="Fridolin">What's got into that fellow?</said> <rs
            ref="#Fridolin">Fridolin</rs> thought, and involuntarily he stopped. The other took two
          more steps and turned. They looked at each other for a moment with only a short distance
          separating them. Suddenly <rs ref="#Fridolin">
            Fridolin</rs> turned around again and went on. He heard a short laugh behind him and he
          longed to challenge the fellow, but he felt his heart beating strangely, just as it had on
          a previous occasion, twelve or fourteen years before. There had been an unusually loud
          knock on his door while he had had with him a certain charming young creature who was
          never tired of prattling about her jealous fiance. As a matter of fact, it was only the
          postman who had knocked in such a threatening manner. And now he felt his heart beating
          just as it had at that time. <said
            aloud="false" direct="false" who="Fridolin">What's the meaning of this?</said> he asked
          himself, and he noticed that his knees were shaking a little. <said
            aloud="false" direct="false" who="Fridolin">Am I a coward? Oh! nonsense</said>, he
          reassured himself. <said
            aloud="false" direct="false" who="Fridolin">Why should I go and face a drunken student,
          I, a man of thirty-five, a practising
            physician, a married man and father of a child? Formal challenge! Seconds! A duel! And
          perhaps because of such a silly encounter receive a cut in my arm and be unable to perform
          my professional duties?—Or lose an eye?—Or even get blood-poisoning?—And in a week perhaps
          be in the same position as the man in Schreyvogel Strasse under the brown flannel blanket?
          Coward—?</said> He had fought three sabre duels, and had even been ready to fight a duel
          with pistols, and it wasn't at his request that the matter had been called off. And what
          about his profession! There were dangers lurking everywhere and at all times—except that
          one usually forgets about them. Why, how long ago was it that that child with diphtheria
          had coughed in his face? Only three or four days, that's all. After all, that was much
          more dangerous than a little fencing match with sabres, and he hadn't given it a second
          thought. Well, if he ever met that fellow again, the affair could still be straightened
          out. He was by no means bound by the code of honor to take a silly encounter with a
          student seriously when on an errand of mercy, to or from a patient. But if, for instance,
          he should meet the young Dane with whom <rs
            ref="#Albertina">Albertina</rs>— oh, nonsense, what was he thinking of? Well, after all,
          it was just as bad as if she had been his mistress. Even worse. Yes, just let that fellow
          cross his path! What a joy it would be to face him somewhere in a clearing in the woods
          and aim a pistol at his forehead with its smoothly combed blond hair. He suddenly
          discovered that he had passed his destination. He was in a narrow street in which only a
          few doubtful-looking women were strolling about in a pitiful attempt to bag their game. <said
            aloud="false" direct="false" who="Fridolin">It's phantomlike</said>, he thought. And in
          retrospect the students, too, with their blue caps, suddenly seemed unreal. The same was
          true of <rs ref="#Marianne">Marianne</rs>, her fiance, her uncle and aunt, all of whom he
          pictured standing hand in hand around the deathbed of the old <rs ref="councilor">
          Councilor</rs>. <rs
            ref="#Albertina">Albertina</rs>, too, whom he could see in his mind's eye soundly
          sleeping, her arms folded under her head—even his child lying in the narrow white brass
          bed, rolled up in a heap, and the red-cheeked governess with the mole on her left
          temple—all of them seemed to belong to another world. Although this idea made him shudder
          a bit, it also reassured him, for it seemed to free him from all responsibility, and to
          loosen all the bonds of human relationship. <rs ref="#Mizzi">One of the girls</rs>
          wandering about stopped him. She was still a young and pretty little thing, very pale with
          red-painted lips. <said
            aloud="false" direct="false" who="Fridolin">She also
            might lead to a fatal end, only not as quickly</said>, he thought. <said
            aloud="false" direct="false" who="Fridolin">Is this cowardice too? I
            suppose really it is</said>. He heard her steps and then her voice behind him. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">Won't you come
            with me, doctor?"</said> He turned around involuntarily. <said
            aloud="true" direct="true" who="Fridolin" listener="Mizzi">"How do you know who I am?"</said>
          he asked. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"Why, I don't know you,"</said>
          she said, <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"but here in this part of
            town they're all doctors, aren't they?"</said> He had had no relations with a woman of
          this sort since he had been a student at the Gymnasium. Was the attraction this girl had
          for him a sign that he was suddenly reverting to adolescence? He recalled a casual
          acquaintance, a smart young man, who was supposed to be extremely successful with women.
          Once while <rs ref="#Fridolin">
            Fridolin</rs> was a student he had been sitting with him in an all-night cafe, after a
          ball. When the young man proposed to leave with one of the regular girls of the place, <rs
            ref="#Fridolin">Fridolin</rs> looked at him in surprise. Thereupon he answered: <said
            aloud="true" direct="true" who="Fridolin" listener="Mizzi">"After
            all, it's the most convenient way— and they aren't by any means the worst." "What's your
          name?"</said> <rs ref="#Fridolin">Fridolin</rs> asked the girl. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"Well, what do you think?
          Mizzi,
            of course."</said> She unlocked the house-door, stepped into the hallway and waited for <rs
            ref="#Fridolin">Fridolin</rs> to follow her. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"Come on,"</said> she said
          when he hesitated. He stepped in beside her, the door closed behind him, she locked it,
          lit a wax candle and went ahead, lighting the way.<said
            aloud="false" direct="false" who="Fridolin">—Am I mad?</said> he asked himself. Of
          course I shall have nothing to do with her. An oil-lamp was burning in her room, and she
          turned it up. It was a fairly pleasant place and neatly kept. At any rate, it smelled
          fresher than <rs ref="#Marianne">
            Marianne</rs>'s home, for instance. But then, of course, no old man had been lying ill
          there for months. <rs ref="#Mizzi">The girl</rs> smiled, and without forwardness
          approached <rs ref="#Fridolin">
            Fridolin</rs> who gently kept her at a distance. She pointed to a rocking-chair into
          which he was glad to drop. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"You must be very tired,"</said>
          she remarked. He nodded. Undressing without haste, she continued: <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"Well, no wonder, with all
            the things a man like you has to do in
            the course of a day. We have an easier time of it."</said> He noticed that her lips were
          not painted, as he had thought, but were a natural red, and he complimented her on that. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"But
            why should I rouge?" she inquired. "How old do you think I am?"</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Mizzi">"Twenty?"</said> <rs
            ref="#Fridolin">Fridolin</rs> ventured. <said
            aloud="true" direct="true" who="Mizzi" listener="Fridolin">"Seventeen,"</said> she said,
          and sat on his lap, putting her arms around his neck like a child. <said
            aloud="false" direct="false" who="Fridolin">Who in the world would suspect that I'm
            here in this room at this moment?</said> <rs
            ref="#Fridolin">Fridolin</rs> thought. <said
            aloud="false" direct="false" who="Fridolin">I'd never have thought it possible an hour
            or
            even ten minutes ago. And— why? Why am I here?</said> Her lips were seeking his, but he
          drew back his head. She looked at him with sad surprise and slipped down from his lap. He
          was sorry, for he had felt much comforting tenderness in her embrace. She took a red
          dressing-gown which was hanging over the foot of the open bed, slipped into it and folded
          her arms over her breast so that her entire body was concealed. <said aloud="true"
            direct="true" who="Mizzi" listener="Fridolin">"Does this suit you better?"</said> she
          asked without mockery, almost timidly, as though making an effort to understand him. He
          hardly knew what to answer. <said aloud="true"
            direct="true" who="Fridolin" listener="Mizzi">"You're right,"</said> he said. <said
            aloud="true"
            direct="true" who="Fridolin" listener="Mizzi">"I am really tired, and I find it
            very pleasant sitting here in the rocking-chair and simply listening to you. You have
          such
            a nice gentle voice. Just talk to me."</said> She sat down on the couch and shook her
          head. <said aloud="true"
            direct="true" who="Mizzi" listener="Fridolin">"You're simply afraid,"</said> she said
          softly —and then to herself in a barely audible voice: <said aloud="true"
            direct="true" who="Mizzi">"It's too bad."</said> These last words made the blood race
          through his veins. He walked over to her, longing to touch her, and declared that he
          trusted her implicitly and saying so he spoke the truth. He put his arms around her and
          wooed her like a sweetheart, like a beloved woman, but she resisted, until he felt ashamed
          and finally gave it up. She explained: <said aloud="true"
            direct="true" who="Mizzi" listener="Fridolin">"You never can tell, some time or other
          it's bound to get out.
            It's quite right of you to be afraid. If something should happen, you would curse me."</said>
          She was so positive in refusing the banknotes which he offered her that he did not insist.
          She put a little blue woolen shawl about her shoulders, lit a candle to light him
          downstairs, went down with him and unlocked the door. <said aloud="true"
            direct="true" who="Mizzi" listener="Fridolin">"I'm not going out any more tonight,"</said>she
          said. He took her hand and involuntarily kissed it. She looked up to him astonished,
          almost frightened. Then she laughed, embarrassed and happy. <said aloud="true"
            direct="true" who="Mizzi" listener="Fridolin">"Just as if I were a young lady,"</said>
          she said. The door closed behind <rs ref="#Fridolin">Fridolin</rs> and he quickly made a
          mental note of the street number, so as to be able to send the poor little thing some wine
          and cakes the following day. </p>
      </div>
      <div type="chapter" n="4">
        <head>4.</head>
        <p> MEANWHILE it had become even milder outside. A fragrance from dewy
        meadows and distant mountains drifted with the gentle breezes into the narrow street. <said
            aloud="false"
            direct="false" who="Fridolin">Where shall I go now? </said><rs
            ref="#Fridolin">Fridolin</rs> asked himself, as though it weren't the obvious thing to
        go home to bed. But he couldn't persuade himself to do so. He felt homeless, an outcast,
        since his annoying meeting with the students ... or was it since <rs ref="#Marianne">
        Marianne</rs>'s confession? No, it was longer than that—ever since this evening's
        conversation with <rs ref="#Albertina">Albertina</rs> he was moving farther and farther away
        from his everyday existence into some strange and distant world. He wandered about aimlessly
        through the dark streets, letting the breeze blow through his hair. Finally, he turned
        resolutely into a third-rate coffee-house. The place was dimly lighted and not especially
        large, but it had an old-fashioned, cozy air about it, and was almost empty at this late
        hour. Three men were playing cards in a corner. The waiter who had been watching them helped <rs
            ref="#Fridolin">Fridolin</rs> take off his fur coat, took his order and placed
        illustrated journals and evening papers on his table. <rs ref="#Fridolin">Fridolin</rs> felt
        slightly more secure and began to look through the papers. His eyes were arrested here and
        there by some news-item. In some Bohemian city, street signs with German names had been torn
        down. There was a conference in Constantinople in which Lord Cranford took part about
        constructing a railway in Asia Minor. The firm Benies &amp; Weingruber had gone into
        bankruptcy. The prostitute Anna Tiger, in a fit of jealousy, had attempted to throw vitriol
        on her friend, Hermine Drobizky. An Ash Wednesday fishdinner was being given that evening in
        Sophia Hall. Marie B., a young girl residing at No. 28 Schonbrunn Strasse, had poisoned
        herself with mercuric chloride.—Prosaically commonplace as they were, all these facts, the
        insignificant as well as the sad, had a sobering and reassuring effect on <rs
            ref="#Fridolin">Fridolin</rs>. He felt sorry for the young girl, Marie B. How stupid to
        take mercuric chloride! At this very moment, while he was sitting snugly in the cafe, while <rs
            ref="#Albertina">Albertina</rs> was calmly sleeping, and the <rs ref="#councilor">
        Councilor</rs>had passed beyond all human suffering, Marie B., No. 28 Schonbrunn Strasse,
        was writhing in incredible pain. He looked up from his paper and encountered the gaze of a
        man seated opposite. <said aloud="false" direct="false" who="Fridolin">Was it possible? <rs
              ref="#Nachtigall">Nachtigall</rs>—?</said> The latter had already recognized him,
        threw up his hands in pleased surprise and joined him at his table. He was still a young
        man, tall, rather broad, and none too thin. His long, blond, slightly curly hair had a touch
        of gray in it, and his moustache drooped in Polish fashion. He was wearing an open gray
        top-coat, underneath which were visible a greasy dress-suit, a crumpled shirt with three
        false diamond studs, a crinkled collar and a dangling, white silk tie. His eyelids were
        inflamed, as if from many sleepless nights, but his blue eyes gleamed brightly. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">You here in Vienna, <rs
              ref="#Nachtigall">Nachtigall</rs>?"</said> exclaimed <rs
            ref="#Fridolin">Fridolin</rs>. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Didn't you know?"</said>
        said <rs ref="#Nachtigall">Nachtigall</rs> with a soft, Polish accent and a slightly Jewish
        twang. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"How could you miss it,
        and me so
            famous?"</said> He laughed loudly and good-naturedly, and sat down opposite <rs
            ref="#Fridolin">Fridolin</rs>. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"What,"</said> asked <rs
            ref="#Fridolin">Fridolin</rs>, <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"have
            you been appointed Professor of Surgery without my hearing of it?"</said> <rs
            ref="#Nachtigall">
            Nachtigall</rs> laughed still louder. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Didn't you hear me just
        now, just a minute ago?"</said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"What do you mean—hear
        you?—Why, of course."</said> Suddenly it occurred to him that someone had been playing the
        piano when he entered; in fact, he had heard music coming from some basement as he
        approached the cafe. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"So that was you
        playing?"</said> he exclaimed. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"It was,"</said> <rs
            ref="#Nachtigall">Nachtigall</rs> said, laughing. <rs
            ref="#Fridolin">Fridolin</rs> nodded. Why, of course—the strangely vigorous touch, the
        peculiar, but euphonious bass chords had at once seemed familiar to him. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Are you devoting
        yourself entirely to it?"</said> he asked. He remembered that <rs ref="#Nachtigall">
        Nachtigall</rs> had definitely given up the study of medicine after his second preliminary
        examination in zoology, which he had passed although he was seven years late in taking it.
        Since then he had been hanging around the hospital, the dissecting room, the laboratories
        and classrooms for some time afterwards. With his blond artist's head, his crinkled collar,
        his dangling tie that had once been white, he had been a striking and, in the humorous
        sense, popular figure. He had been much liked, not only by his fellow-students, but also by
        many professors. The son of a Jewish gin-shop owner in a small Polish town, he had left home
        early and had come to Vienna to study medicine. The trifling sums he received from his
        parents had from the very-beginning been scarcely worth mention and were soon discontinued.
        However, this didn't prevent his appearing in the Riedhof Hotel at the table reserved for
        medical students where <rs
            ref="#Fridolin">Fridolin</rs> was a regular guest. At intervals, one after another of
        his more well-todo fellow-students would pay his bill. He sometimes, also, was given
        clothes, which he accepted gladly and without false pride. He had already learned to play in
        his home town from a pianist stranded there, and while he was a medical student in Vienna he
        had studied at the Conservatory where he was considered a talented musician of great
        promise. But here, too, he was neither serious nor diligent enough to develop his art
        systematically. He soon became entirely content with the impression he made on his
        acquaintances, or rather with the pleasure he gave them by his playing. For a while he had a
        position as pianist in a suburban dancing-school. Fellow-students and table-companions tried
        to introduce him into fashionable houses in the same capacity, but on such occasions he
        would play only what suited him and as long as he chose. His conversations with the young
        girls present were not always harmless, and he drank more than he could carry. Once, playing
        for a dance in the house of a wealthy banker, he embarrassed several couples with flattering
        but improper remarks, and ended up by playing a wild cancan and singing a risque song with
        his powerful, bass voice. The host gave him a severe calling down, but <rs
            ref="#Nachtigall">Nachtigall</rs>, blissfully hilarious, got up and embraced him. The
        latter was furious and, although himself a Jew, hurled a common insult at him. <rs
            ref="#Nachtigall">Nachtigall</rs> at once retaliated with a powerful box on his ears,
        and this definitely concluded his career in the fashionable houses of the city. He behaved
        better, on the whole, in more intimate circles, although sometimes when the hour was late,
        he had to be put out of the place by force. But the following morning all was forgiven and
        forgotten. One day, long after his friends had graduated, he disappeared from the city
        without a word. For a few months he sent post cards from various Russian and Polish cities,
        and once <rs
            ref="#Fridolin">Fridolin</rs>, who was one of <rs ref="#Nachtigall">Nachtigall</rs>'s
        favorites, was reminded of his existence not only by a card, but by a request for a moderate
        sum of money, without explanation. <rs ref="#Fridolin">Fridolin</rs> sent it at once, but
        never received a word of thanks or any other sign of life from <rs
            ref="#Nachtigall">Nachtigall</rs>. At this moment, however, eight years later, at a
        quarter to one in the morning, <rs ref="#Nachtigall">Nachtigall</rs> insisted on paying his
        debt, and took the exact amount in bank-notes from a rather shabby pocket-book. As the
        latter was fairly well filled, <rs ref="#Fridolin">Fridolin</rs> accepted the repayment with
        a good conscience. <said aloud="true" direct="true" who="Fridolin"
            listener="Nachtigall">Are you getting along well,"</said> he asked with a smile, in
        order to make sure. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"I can't complain,"</said>
        replied <rs ref="#Nachtigall">Nachtigall</rs>. Placing his hand on <rs ref="#Fridolin">
        Fridolin</rs>'s arm, he continued: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"But tell me, why are
            you
            here so late at night?"</said> <rs ref="#Fridolin">
            Fridolin</rs> explained that <said aloud="true" direct="false" who="Fridolin"
            listener="Nachtigall">he had needed a cup of coffee after visiting a patient,
            although he didn't say, without quite knowing why, that he hadn't found his patient
        alive.
            Then he talked in very general terms of his duties at the hospital and his private
        practice, and mentioned that he was happily married, and the father of a six-year old
            girl.</said> <rs ref="#Nachtigall">Nachtigall</rs> in his turn, <said aloud="true"
            direct="false" who="Nachtigall" listener="Fridolin">explained that he had spent the time
        as a pianist in every possible sort of Polish, Roumanian, Serbian and Bulgarian city and
        town, just as <rs
              ref="#Fridolin">Fridolin</rs> had surmised. He had a wife and four children living in
        Lemberg, and he laughed heartily, as though it were unusually jolly to have four children,
        all of them living in Lemberg, and all by one and the same woman. He had been back in Vienna
        since the preceding fall. The vaudeville company he had been with had suddenly gone to
        pieces. He was now playing anywhere and everywhere, anything that happened to come along,
        sometimes in two or three different houses the same night. For example, down there in that
        basement—not at all a fashionable place, as he remarked, really a sort of bowling alley, and
        with very doubtful patrons. . . .</said><said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin"> "But if you have to
        provide for four children
            and a wife in Lemberg"—he laughed again, though not quite as gaily as before, and added:
        "But sometimes I am privately engaged."</said> Noticing a reminiscent smile on <rs
            ref="#Fridolin">Fridolin</rs>'s face, he continued: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Not just in the houses
        of bankers
            and such, but in all kinds of circles, even larger ones, both public and secret."</said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Secret?</said>" <rs
            ref="#Fridolin">Fridolin</rs> asked. <rs ref="#Nachtigall">Nachtigall</rs> looked
        straight before him with a gloomy and crafty air, and said: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"They will be calling
            for me
            again in a minute."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"What, are you playing
        somewhere else tonight?"</said> <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Yes, they only begin
        there at two."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"It must be an unusually
        smart place."</said> <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Yes and no,"</said>
        said <rs
            ref="#Nachtigall">Nachtigall</rs>, laughing, but he became serious again at once. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Yes
            and no?"</said> queried <rs ref="#Fridolin">Fridolin</rs>, curiously. <rs
            ref="#Nachtigall">
            Nachtigall</rs> bent across the table. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"I'm playing tonight in
            a private house, but I
            don't know whose it is."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Then you're playing
        there for the first time?"</said> <rs
            ref="#Fridolin">
            Fridolin</rs> asked with increasing interest. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"No, it's the third
            time, but it will
            probably be a different house again."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"I don't understand."</said> <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Neither do I,"</said>
        said <rs
            ref="#Nachtigall">Nachtigall</rs>, laughing, <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"but you'd better not
            ask any more."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Oh, I
            see,"</said> remarked <rs
            ref="#Fridolin">Fridolin</rs>. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"No, you're wrong. It's
        not what you think. I've seen a
            great deal in my time. It's unbelievable what one sees in such small towns, especially
            in
            Roumania, but here . . ."</said> He drew back the yellow curtain from the window, looked
        out on the street and said as if to himself: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Not here yet."</said>
        Then he turned to <rs
            ref="#Fridolin">Fridolin</rs> and explained: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"I mean the carriage.
        There's always a
            carriage to call for me, a different one each time."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"You're making me very
        curious, <rs
              ref="#Nachtigall">Nachtigall</rs>,"</said> <rs ref="#Fridolin">Fridolin</rs> assured
        him. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Listen to me,"</said>
        said <rs ref="#Nachtigall">Nachtigall</rs> after a slight pause. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"I'd like
            to be able to arrange it—'but how can I do it—"</said> Suddenly he burst out: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Have you got
            plenty of nerve?"</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"That's a strange
        question,"</said> said <rs
            ref="#Fridolin">Fridolin</rs> in the tone of an offended fraternity student. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"I don't
            mean that."</said> <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Well, what do you
        mean?—Why does one need so much courage for this affair?
            What can possibly happen?"</said> He gave a short and contemptuous laugh. <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Nothing can happen to
        me. At best this would be the last time—but perhaps that may be the case anyhow."</said> He
        stopped and looked out again through the crevice in the curtain. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Well, then where's the
        difficulty?"</said> <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"What did you say?"</said>
        asked <rs ref="#Nachtigall">Nachtigall</rs>, as if coming out of a dream. <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Tell me the rest of the
        story, now that you've started. A secret party?
            Closed affair? Nothing but invited guests?"</said>
        </p> [START ERICA PART 2] <p>
          <said aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"I don't know. The
        last time there were thirty people, and the first time only sixteen."</said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"A ball?"</said> 
          <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Of course, a ball."</said>
        He seemed to be sorry he had spoken of the matter at all. <said aloud="true" direct="true"
            who="Fridolin" listener="Nachtigall">"And you're furnishing the music for the occasion?"</said>
          <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"What do you mean—for
            the occasion? I don't know for what occasion. I simply play—with bandaged
            eyes."</said>
          <said aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"<rs
              ref="#Nachtigall" type="character">Nachtigall</rs>, what do you mean?"</said>
          <rs
            ref="#Nachtigall" type="character">Nachtigall</rs> sighed a little and continued: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Unfortunately my eyes
        are not completely bandaged, so that
            I can occasionally see something. I can see through the black silk handkerchief over my
        eyes in the mirror
            opposite. . . ."</said> And he stopped. <said aloud="true" direct="true" who="Fridolin"
            listener="Nachtigall">"In other words,"</said> said Fridolin impatiently and
        contemptuously, but feeling strangely excited, <said aloud="true" direct="true"
            who="Fridolin" listener="Nachtigall">"naked
            females."</said>
          <said aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Don't
        say females,"</said> replied <rs ref="#Nachtigall" type="character">Nachtigall</rs> in an
        offended tone, <said aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"you
        never saw such women."</said>
          <rs ref="#Fridolin" type="character">Fridolin</rs> hemmed and
        hawed a little. <said aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"And
        what's the price of admission?"</said> he asked casually. <said aloud="true" direct="true"
            who="Nachtigall" listener="Fridolin">"Do you mean tickets and such? There are none."</said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Well, how does one gain
        admittance?"</said> asked <rs ref="#Fridolin" type="character">Fridolin</rs> with compressed
        lips and tapping on the table with his fingers. <said aloud="true" direct="true"
            who="Nachtigall" listener="Fridolin">"You have to know the password, and it's a new one
        each time."</said>
          <said aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"And
        what's the one for tonight?"</said>
          <said aloud="true" direct="true" who="Nachtigall"
            listener="Fridolin">"I don't know yet. I'll only find out from the coachman."</said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Take me along,
        Nachtigall."</said>
          <said aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Impossible.
        It's too dangerous."</said> 
          <said aloud="true" direct="true" who="Fridolin"
            listener="Nachtigall">"But a minute ago you yourself spoke ... of being willing to ... I
        think you can manage all right."</said>
        </p>
        <p>
          <rs ref="#Nachtigall" type="character">Nachtigall</rs> looked at him critically and said: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"It would be absolutely
        impossible in your street clothes,
            for everyone is masked, men and women. As you haven't a masquerade outfit with you, it's
        out of the
            question. Perhaps the next time. I'll try to figure out some way."</said> He listened
        attentively, peered again through the opening in the curtain and said with a sigh of relief: <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"There's my carriage,
        good-bye."</said>
        </p>
        <p>
          <rs ref="#Fridolin" type="character">Fridolin</rs> hung on to his arm and said: <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"You can't get away that
        way. You've got to take me along."</said>
          <said aloud="true" direct="true" who="Nachtigall"
            listener="Fridolin">"But my dear man . . ."</said>
          <said aloud="true" direct="true"
            who="Fridolin" listener="Nachtigall">"Leave it to me. I know that it's dangerous.
            Perhaps that's the very thing that tempts me."</said> 
          <said aloud="true" direct="true"
            who="Nachtigall" listener="Fridolin">"But I've already told you—without costume and
        mask———"</said>
          <said aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"There
        are places to rent costumes."</said>
          <said aloud="true" direct="true" who="Nachtigall"
            listener="Fridolin">"At one o'clock in the morning?"</said>
          <said aloud="true"
            direct="true" who="Fridolin" listener="Nachtigall">"Listen here, <rs ref="#Nachtigall"
              type="character">Nachtigall</rs>. There's just such a place at the corner of
        Wickenburg Strasse. I walk past it several times a day."</said> And he added, with growing
        excitement: <said aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"You stay
        here for another quarter of an hour, <rs ref="#Nachtigall" type="character">Nachtigall</rs>.
        In the meantime I'll see what luck I have. The proprietor of the costume shop probably lives
        in the same building. If he doesn't—well, then I'll simply give it up for tonight. Let fate
        decide the question. There's a cafe in the same building. I think it's called Cafe
        Vindobona. You tell the coachman that you've forgotten something in the cafe, walk in, and
        I'll be waiting near the door. Then you can give me the password and get back into your
        carriage. If I manage to get a costume I'll take a cab and immediately follow you. The rest
        will take care of itself. I give you my word of honor, <rs ref="#Nachtigall"
              type="character">Nachtigall</rs>, that if you run any risk, I'll assume complete
        responsibility."</said>
          <rs ref="#Nachtigall" type="character">Nachtigall</rs> had tried
        several times to interrupt <rs ref="#Fridolin" type="character">Fridolin</rs>, but it was
        useless—— </p>
        <p> The former threw some money on the table to pay his bill, including a
        generous tip which seemed appropriate for the style of the night, and left. A closed
        carriage was standing outside. A coachman dressed entirely in black with a tall silk hat,
        sat on the box, motionless. It looks like a mourning-coach, <rs ref="#Fridolin"
            type="character">Fridolin</rs> thought. He ran down the street and reached the
        corner-house he was looking for a few minutes later. He rang the bell, inquired from the
        care-taker whether the costumer <rs ref="#Gibiser" type="character">Gibiser</rs> lived in
        the house, and hoped in the bottom of his heart that he would receive a negative answer. But <rs
            ref="#Gibiser" type="character">Gibiser</rs> actually lived there, on the floor below
        that of the costume shop. The care-taker did not seem especially surprised at having such a
        late caller. Made affable by <rs ref="#Fridolin" type="character">Fridolin</rs>'s liberal
        tip, he stated that it was not unusual during the carnival for people to come at such a late
        hour to hire costumes. He lighted the way from below with a candle until <rs ref="#Fridolin"
            type="character">Fridolin</rs> had rung the bell on the second floor.<rs ref="#Gibiser"
            type="character">Herr Gibiser</rs> himself opened the door for him, as if he had been
        waiting there. He was a bald-headed, haggard man and wore an old-fashioned, flowered
        dressing-gown and a tasselled, Turkish cap which made him look like a foolish old man on the
        stage. <rs ref="#Fridolin" type="character">Fridolin</rs> asked for a costume and said that
        the price did not matter, whereupon <rs ref="#Gibiser" type="character">Herr Gibiser</rs>
        remarked, almost disdainfully: <said aloud="true" direct="true" who="Gibiser"
            listener="Fridolin">"I ask a fair price, no more."</said>
        </p>
        <p> He led the way
        up a winding staircase into the store. There was an odor of silk, velvet, perfume, dust and
        withered flowers, and a glitter of silver and red out of the indistinct darkness. A number
        of little electric bulbs suddenly shone between the open cabinets of a long, narrow passage,
        the end of which was enveloped in darkness. There were all kinds of costumes hanging to the
        right and to the left. On one side knights, squires, peasants, hunters, scholars, Orientals
        and clowns; on the other, ladies-at-court, baronesses, peasant women, lady's maids, queens
        of the night. The corresponding head-dresses were on a shelf above the costumes. <rs
            ref="#Fridolin" type="character">Fridolin</rs> felt as though he were walking through a
        gallery of hanged people who were on the point of asking each other to dance. <rs
            ref="#Gibiser" type="character">Herr Gibiser</rs> followed him. Finally he asked: <said
            aloud="true" direct="true" who="Gibiser" listener="Fridolin">"Is
            there anything special you want? Louis Quatorze, Directoire, or Old-German?</said>
        </p>
        <p>
          <said aloud="true" direct="true" who="Fridolin" listener="Gibiser">"I need a dark cassock
        and a black mask, that's all."</said> At this moment the clink of glasses rang out from the
        end of the passage. <rs ref="#Fridolin" type="character">Fridolin</rs> was startled and
        looked at the costumer, as though he felt an explanation were due. <rs ref="#Gibiser"
            type="character">Gibiser</rs>, however, merely groped for a switch which was concealed
        somewhere. A blinding light was diffused over the entire passage down to the end where a
        little table, covered with plates, glasses and bottles, could be seen. Two men, dressed in
        the red robes of vehmic judges, sprang up from two chairs beside the table and a graceful
        little girl disappeared at the same moment. <rs ref="#Gibiser" type="character">Gibiser</rs>
        rushed forward with long strides, reached across the table and grabbed a white wig in his
        hand. Simultaneously a young and charming girl, still almost a child, wearing a Pierrette
        costume, wriggled out from under the table and ran along the passage to <rs ref="#Fridolin"
            type="character">Fridolin</rs> who caught her in his arms. <rs ref="#Gibiser"
            type="character">Gibiser</rs> dropped the white wig and grabbed the two vehmic judges by
        their robes. At the same time he called out to <rs ref="#Fridolin" type="character">Fridolin</rs>
        : <said aloud="true" direct="true" who="Gibiser" listener="Fridolin">"Hold on to that girl
        for me."</said> The child pressed against <rs ref="#Fridolin" type="character">Fridolin</rs>
        as though sure of protection. Her little oval face was covered with powder and several
        beauty spots, and a fragrance of roses and powder arose from her delicate breasts. There was
        a smile of impish desire in her eyes. </p>
        <p>
          <said aloud="true" direct="true" who="Gibiser" listener="Gentlemen">"Gentlemen,"</said>
        cried <rs ref="#Gibiser" type="character">Gibiser</rs>, <said aloud="true" direct="true"
            who="Gibiser" listener="Fridolin">"you will stay here while I call the police."</said>
          <said
            aloud="true" direct="true" who="Gentlemen" listener="Gibiser">"What's got into you?"</said>
        they exclaimed, and continued as if with one voice: <said aloud="true" direct="true"
            who="Gentlemen" listener="Gibiser">"We were invited by the
            young lady."</said>
          <rs ref="#Gibiser" type="character">Gibiser</rs> released his hold
        and <rs ref="#Fridolin" type="character">Fridolin</rs> heard him saying: <said aloud="true"
            direct="true" who="Gibiser" listener="Gentlemen">"You will have to explain this.
            Couldn't you see
            that the girl was deranged?"</said> Then turning to <rs ref="#Fridolin" type="character">
        Fridolin</rs>, he said: <said aloud="true" direct="true" who="Gibiser" listener="Fridolin">"Sorry
        to keep you waiting."</said> 
          <said aloud="true" direct="true" who="Fridolin"
            listener="Gibiser">"Oh, it doesn't matter,"</said> said <rs ref="#Fridolin"
            type="character">Fridolin</rs>. He would have liked to stay, or, better still, to take
        the girl with him, no matter where —and whatever the consequences. She looked up at him with
        alluring and child-like eyes, as if spellbound. The men at the end of the passage were
        arguing excitedly. <rs ref="#Gibiser" type="character">Gibiser</rs> turned to <rs
            ref="#Fridolin" type="character">Fridolin</rs> and asked in a matter-of-fact way: <said
            aloud="true" direct="true" who="Gibiser" listener="Fridolin">"You wanted a cassock, a
        pilgrim's hat and a mask?"</said> 
          <said aloud="true" direct="true" who="Pierrette"
            listener="Gibiser">"No,"</said> said <rs ref="#Pierrette" type="character">Pierrette</rs>
        with gleaming eyes, <said aloud="true" direct="true" who="Pierrette" listener="Gibiser">"you
        must give this gentleman a cloak lined with ermine and a
            doublet of red silk."</said>
          <said aloud="true" direct="true" who="Gibiser"
            listener="Pierrette">"Don't you budge from my side,"</said> answered <rs ref="#Gibiser"
            type="character">Gibiser</rs>. Then he pointed to a dark frock hanging between a
        medieval soldier and a Venetian Senator, and said: <said aloud="true" direct="true"
            who="Gibiser" listener="Fridolin">"That's about your size and here's the hat. Take it
        quick."</said> The two strange men protested again: <said aloud="true" direct="true"
            who="Gentlemen" listener="Gibiser">"You'll have to let us out at once, <rs
              ref="#Gibiser" type="character">Herr Chibisier</rs>."</said> <rs ref="#Fridolin"
            type="character">Fridolin</rs> noticed with surprise the French pronunciation of the
        name <rs ref="#Gibiser" type="character">Gibiser</rs>. <said aloud="true" direct="true"
            who="Gibiser" listener="Gentlemen">"That's out of the question,"</said> replied the
        costumer scornfully. <said aloud="true" direct="true" who="Gibiser" listener="Gentlemen">"You'll
        kindly wait here until I return."</said> Meanwhile <rs ref="#Fridolin" type="character">
        Fridolin</rs> slipped into the cassock and tied the white cords. <rs ref="#Gibiser"
            type="character">Gibiser</rs>, who was standing on a narrow ladder, handed him the
        black, broad-rimmed pilgrim's hat, and he put it on. But he did all this unwillingly, being
        more and more convinced that danger was threatening <rs ref="#Pierrette" type="character">
        Pierrette</rs> and that it was his duty to remain and help her. The mask which <rs
            ref="#Gibiser" type="character">Gibiser</rs> gave him and which he at once tried on,
        smelt strange and rather disagreeable. <said aloud="true" direct="true" who="Gibiser"
            listener="Pierrette">"You walk down ahead of me,"</said> <rs ref="#Gibiser"
            type="character">Gibiser</rs> commanded the girl, pointing to the stairs. <rs
            ref="#Pierrette" type="character">Pierrette</rs> turned and waved a gay, yet wistful
        farewell. <rs ref="#Fridolin" type="character">Fridolin</rs>'s eyes followed the direction
        of her gaze. The two men were no longer in costume but wore evening clothes and white ties,
        though their faces were still covered by their red masks. <rs ref="#Pierrette"
            type="character">Pierrette</rs> went down the winding staircase with a light step, <rs
            ref="#Gibiser" type="character">Gibiser</rs> behind her and <rs ref="#Fridolin"
            type="character">Fridolin</rs> following in the rear. In the anteroom below <rs
            ref="#Gibiser" type="character">Gibiser</rs> opened a door leading to the inner rooms
        and said to <rs ref="#Pierrette" type="character">Pierrette</rs>: <said aloud="true"
            direct="true" who="Gibiser" listener="Pierrette">"Go to bed at once, you depraved
        creature. I'll talk to you as soon as I've settled
            with those two upstairs."</said> She stood in the doorway, white and delicate, and with
        a glance at <rs ref="#Fridolin" type="character">Fridolin</rs>, sadly shook her head. He
        noticed with surprise, in a large wall-mirror to the right, a haggard pilgrim who seemed to
        be himself. At the same time he knew very well that it could be no other. The girl
        disappeared and the old costumer locked the door behind her. Then he opened the entrance
        door and hurried <rs ref="#Fridolin" type="character">Fridolin</rs> out into the hallway. <said
            aloud="true" direct="true" who="Fridolin" listener="Gibiser">"Well,"</said> said <rs
            ref="#Fridolin" type="character">Fridolin</rs>, <said aloud="true" direct="true"
            who="Fridolin" listener="Gibiser">"how much do I owe you?"</said>
          <said aloud="true"
            direct="true" who="Gibiser" listener="Fridolin">"Never mind, sir, you can pay when you
        return the things. I'll trust you." </said>
          <rs ref="#Fridolin" type="character">Fridolin</rs>,
        however, refused to move. <said aloud="true" direct="true" who="Fridolin" listener="Gibiser">"Swear
        that you won't hurt that poor child,"</said> he said. <said aloud="true" direct="true"
            who="Gibiser" listener="Fridolin">"What business is it of yours?"</said> 
          <said
            aloud="true" direct="true" who="Fridolin" listener="Gibiser">"I heard you, a minute ago,
        say that the girl was insane—and just now you called her a depraved
            creature. That sounds pretty contradictory." </said>
          <said aloud="true" direct="true"
            who="Gibiser" listener="Fridolin">"Well,"</said> replied <rs ref="#Gibiser"
            type="character">Gibiser</rs> theatrically, <said aloud="true" direct="true"
            who="Gibiser" listener="Fridolin">"aren't insanity and depravity the same in the eyes of
        God?" </said>
          <rs ref="#Fridolin" type="character">Fridolin</rs> shuddered with disgust. <said
            aloud="true" direct="true" who="Fridolin" listener="Gibiser">"Whatever it is,"</said> he
        remarked, <said aloud="true" direct="true" who="Fridolin" listener="Gibiser">"there are ways
        and means of attending to it. I am a doctor. We'll have
            another talk about this tomorrow." </said>
          <rs ref="#Gibiser" type="character">Gibiser</rs>
        laughed mockingly without uttering a sound. A light flared up in the hallway, and the door
        between them was closed and immediately bolted. <rs ref="#Fridolin" type="character">
        Fridolin</rs> took off the hat, cassock and mask while going downstairs, carrying the bundle
        under his arm. The care-taker opened the outer door and <rs ref="#Fridolin" type="character">
        Fridolin</rs> saw the mourning-coach standing opposite with the motionless driver on the
        box. <rs ref="#Nachtigall" type="character">Nachtigall</rs> was just on the point of leaving
        the cafe, and seemed somewhat taken aback at seeing <rs ref="#Fridolin" type="character">
        Fridolin</rs> at hand so promptly. <said aloud="true" direct="true" who="Nachtigall"
            listener="Fridolin">"Then you did manage to get a costume?"</said> 
          <said aloud="true"
            direct="true" who="Fridolin" listener="Nachtigall">"You can see for yourself. What's the
        password?"</said>
          <said aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"You
        insist on knowing it?" </said>
          <said aloud="true" direct="true" who="Fridolin"
            listener="Nachtigall">"Absolutely." </said>
          <said aloud="true" direct="true"
            who="Nachtigall" listener="Fridolin">"Well then—it's Denmark." </said>
          <said aloud="true"
            direct="true" who="Fridolin" listener="Nachtigall">"Are you mad, Nachtigall?" </said>
          <said
            aloud="true" direct="true" who="Nachtigall" listener="Fridolin">"Why mad?" </said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="Nachtigall">"Oh, never mind—I was at
        the seashore in Denmark this summer. Get back into your carriage—but not
            too fast, so that I'll have time to take a cab over on the other side." </said>
          <rs
            ref="#Nachtigall" type="character">Nachtigall</rs> nodded and leisurely lighted a
        cigarette. <rs ref="#Fridolin" type="character">Fridolin</rs> quickly crossed the street,
        hailed a cab in an offhand way, as though he were playing a joke, and told the driver to
        follow the mourning-coach which was just starting in front of them. </p>
        <p> They crossed
        Alser Strasse, and drove on through dim, deserted side-streets under a railroad viaduct
        toward the suburbs. <rs ref="#Fridolin" type="character">Fridolin</rs> was afraid that the
        driver might lose sight of the carriage, but whenever he put his head out of the open
        window, into the abnormally warm air, he always saw it. It was a moderate distance ahead of
        them, and the coachman with his high, black silk hat sat motionless on the box. This
        business may end badly, thought <rs ref="#Fridolin" type="character">Fridolin</rs>. At the
        same time he remembered the fragrance of roses and powder that had arisen from <rs
            ref="#Pierrette" type="character">Pierrette</rs>'s breasts. <said aloud="false"
            direct="false" who="Fridolin" listener="Fridolin">What strange story is behind all that?</said>
        he wondered. <said aloud="false" direct="false" who="Fridolin" listener="Fridolin">I
        shouldn't have
            left—perhaps it was even a great mistake—I wonder where I am now. </said> The road wound
        slowly up-hill between modest villas. <rs ref="#Fridolin" type="character">Fridolin</rs>
        thought that he now had his bearings. He had sometimes come this way on walks, years ago. It
        must be the Galitzinberg that he was going up. Down to his left he could see the city
        indistinct in the mist, but glimmering with a thousand lights. He heard the rumbling of
        wheels behind him and looked out of the window back of him. There were two carriages
        following his. He was glad of that, for now the driver of the mourning-coach would certainly
        not be suspicious of him. With a violent jolt, the cab turned into a side street and went
        down into something like a ravine, between iron fences, stone walls and terraces. <rs
            ref="#Fridolin" type="character">Fridolin</rs> realized that it was high time to put on
        his costume. He took off his fur coat and slipped into the cassock, just as he slipped into
        the sleeves of his white linen coat every morning in his ward at the hospital. He was
        relieved to think that, if everything went well, it would be only a few hours before he
        would be back again by the beds of his patients, ready to give aid. </p>
        <p> His cab stopped. <said
            aloud="false" direct="false" who="Fridolin" listener="Fridolin">What if I don't get out
        at all,</said> <rs ref="#Fridolin" type="character">Fridolin</rs> thought, <said
            aloud="false" direct="false" who="Fridolin" listener="Fridolin">and go back at once? But
        go where? To little <rs ref="#Pierrette" type="character">Pierrette</rs>? To the girl in
        Buchfeld Strasse? Or to <rs
              ref="#Marianne" type="character">Marianne</rs>, the daughter of the deceased? Or
        perhaps home?</said> He shuddered slightly and decided he'd rather go anywhere than home.
        Was it because it was farthest to go? <said aloud="false" direct="false" who="Fridolin"
            listener="Fridolin">No, I can't turn back</said>, he thought. <said aloud="false"
            direct="false" who="Fridolin" listener="Fridolin">I must go through with this, even if
            it means
            death.</said> And he laughed at himself, using such a big word but without feeling very
        cheerful about it. </p>
        <p> A garden gate stood wide open. The mourning-coach drove on deeper
        into the ravine, or into the darkness that seemed like one. <rs ref="#Nachtigall"
            type="character">Nachtigall</rs> must, therefore, have got out. <rs ref="#Fridolin"
            type="character">Fridolin</rs> quickly sprang out of the cab and told the driver to wait
        for him up at the turn, no matter how late he might be. To make sure of him, he paid him
        well in advance and promised him a large sum for the return trip. The other carriages drove
        up and <rs ref="#Fridolin" type="character">Fridolin</rs> saw the veiled figure of a woman
        step out of the first. Then he turned into the garden and put on his mask. A narrow path,
        lighted up by a lamp from the house, led to the entrance. </p>
        <p> Doors opened before him,
        and he found himself in a narrow, white vestibule. He could hear an organ playing, and <rs
            ref="#TWOServants" type="character">two servants</rs> in dark livery, their faces
        covered by gray masks, stood on each side of him. Two voices whispered in unison: <said
            aloud="true"
            direct="true" who="TWOServants" listener="Fridolin">"Password?"</said> He replied: <said
            aloud="true" direct="true" who="Fridolin" listener="TWOServants">"Denmark."</said> One
        of them took his fur coat and disappeared with it into an adjoining room, while the other
        opened a door. <rs ref="#Fridolin" type="character">Fridolin</rs> entered a dimly lighted
        room with high ceilings, hung on all sides with black silk. Sixteen to twenty people masked
        and dressed as monks and nuns were walking up and down. The gently swelling strains of
        Italian church music came from above. A small group, composed of three nuns and two monks,
        stood in a corner of the room. They watched him for a second, but turned away again at once,
        almost deliberately. <rs ref="#Fridolin" type="character">Fridolin</rs>, noticing that he
        was the only one who wore a hat, took his off and walked up and down as nonchalantly as
        possible. A monk brushed against him and nodded a greeting, but from behind the mask <rs
            ref="#Fridolin" type="character">Fridolin</rs> encountered a searching and penetrating
        glance. A strange, heavy perfume, as of Southern gardens, scented the room. Again an arm
        brushed against him, but this time it was that of a nun. Like all the others she had a black
        veil over her face, head and neck, a blood-red mouth glowed under the black laces of the
        mask. <said aloud="false" direct="false" who="Fridolin" listener="Fridolin">Where am I?</said>
        thought <rs ref="#Fridolin" type="character">Fridolin</rs>. <said aloud="false"
            direct="false" who="Fridolin" listener="Fridolin">Among lunatics? Or conspirators? Is
        this a meeting of some religious sect? Can it be that <rs ref="#Nachtigall" type="character">
        Nachtigall</rs> was ordered or paid to bring along some stranger to be the target of their
        jokes?</said> But everything seemed too serious, too intense, too uncanny for a masquerade
        prank. A <rs ref="woman" type="character">woman</rs>'s voice joined the strains of the organ
        and an Old. Italian sacred aria resounded through the room. They all stood still and
        listened and <rs ref="#Fridolin" type="character">Fridolin</rs> surrendered himself for a
        moment to the wondrously swelling melody. A soft voice suddenly whispered from behind: <said
            aloud="true" direct="true" who="woman" listener="Fridolin">"Don't turn around. There's
        still a chance for you to get away. You don't belong here. If it's discovered it will go
            hard with you." </said>
          <rs ref="#Fridolin" type="character">Fridolin</rs> gave a
        frightened start. For a second he thought of leaving, but his curiosity, the allurement and,
        above all, his pride, were stronger than any of his misgivings. Now that I've gone this far,
        he thought, <said aloud="false" direct="false" who="Fridolin" listener="Fridolin">I don't
        care
            what happens</said>. And he shook his head negatively without turning around. The voice
        behind him whispered: <said aloud="true" direct="true" who="woman" listener="Fridolin">"I
        should feel very sorry for you."</said> He turned and looked at her. He saw the blood-red
        mouth glimmering under the lace. Dark eyes were fixed on him. <said aloud="true"
            direct="true" who="Fridolin" listener="woman">"I shall stay,"</said> he said in a heroic
        voice which he hardly recognized as his own, and he looked away again. The song was now
        ringing through the room; the organ had a new sound which was anything but sacred. It was
        worldly, voluptuous, and pealing. Looking around <rs ref="#Fridolin" type="character">
        Fridolin</rs> saw that all the nuns had disappeared and that only the monks were left. The
        voice had meanwhile also changed. It rose by way of an artistically executed trill from its
        low and serious pitch to a high and jubilant tone. In place of the organ a piano had
        suddenly chimed in with its worldly and brazen tunes. <rs ref="#Fridolin" type="character">
        Fridolin</rs> at once recognized <rs ref="#Nachtigall" type="character">Nachtigall</rs>'s
        wild and inflammatory touch. The woman's voice which had been so reverent a moment before
        had vanished with a last wild, voluptuous outburst through the ceiling, as it were, into
        infinity. Doors opened to the right and left On one side <rs ref="#Fridolin"
            type="character">Fridolin</rs> recognized the indistinct outlines of <rs
            ref="#Nachtigall" type="character">Nachtigall</rs>'s figure; the room opposite was
        radiant with a blaze of light. All the women were standing there motionless. They wore dark
        veils over their heads, faces and necks and black masks over their eyes, but otherwise they
        were completely naked. <rs ref="#Fridolin" type="character">Fridolin</rs>'s eyes wandered
        eagerly from voluptuous to slender bodies, from delicate figures to those luxuriously
        developed. He realized that each of these women would forever be a mystery, and that the
        enigma of their large eyes peering at him from beneath the black masks would remain
        unsolved. The delight of beholding was changed to an almost unbearable agony of desire. And
        the others seemed to experience a similar sensation. The first gasps of rapture had changed
        to sighs that held a note very near anguish. A cry broke out somewhere. Suddenly all of
        them, as though pursued, rushed from the darkened room to the women, who received them with
        wild and wicked laughter. The men were no longer in cassocks, but dressed as cavaliers, in
        white, yellow, blue and red. <rs ref="#Fridolin" type="character">Fridolin</rs> was the only
        one in monk's dress. Somewhat nervously he slunk into the farthest corner, where he was near <rs
            ref="#Nachtigall" type="character">Nachtigall</rs> whose back was turned to him. <rs
            ref="#Nachtigall" type="character">Nachtigall</rs> had a bandage over his eyes, but <rs
            ref="#Fridolin" type="character">Fridolin</rs> thought he could see him peering
        underneath the bandage into the tall mirror opposite. In it the cavaliers with their
        gay-colored costumes were reflected, dancing with their naked partners. A woman came up
        suddenly behind <rs ref="#Fridolin" type="character">Fridolin</rs> and whispered—for no one
        spoke aloud, as if the voices, too, were to remain a secret—: <said aloud="true"
            direct="true" who="another woman" listener="Fridolin">"What is the matter? Why don't you
        dance?" </said>
          <rs ref="#Fridolin" type="character">Fridolin</rs>, seeing two noblemen watch
        fixedly from another corner, suspected that this woman with the boyish and slender figure,
        was sent to put him to the test. In spite of it he meant to dance with her, but at that
        moment another woman left her partner and walked quickly up to him. He knew at once that it
        was the same one who had already warned him. She pretended that she had just seen him and
        whispered, in a voice loud enough to be heard in the other corner: <said aloud="true"
            direct="true" who="woman" listener="Fridolin">"Returned at last!"</said> Laughingly, she
        continued: <said aloud="true" direct="true" who="woman" listener="Fridolin">"All your
            efforts are useless. I know you."</said> Then turning to the woman with the boyish
        figure, she said: <said aloud="true" direct="true" who="woman" listener="another woman">"Let
        me have
            him for just two minutes, then he shall be yours again until morning, if you wish."</said>
        In a softer voice she added: <said aloud="true" direct="true" who="woman"
            listener="Fridolin">"It is really he."</said> The other replied in astonishment: <said
            aloud="true" direct="true" who="another woman" listener="woman">"Really?"</said> and
        with a light step went to join the cavaliers in the corner. Alone with <rs ref="#Fridolin"
            type="character">Fridolin</rs>, the woman cautioned him, <said aloud="true"
            direct="true" who="woman" listener="Fridolin">"Don't ask questions, and don't be
        surprised at
            anything. I tried to lead them astray, but you can't continue to deceive them for long.
        Go, before it is too
            late—and it may be too late at almost any moment—and be careful that no one follows you.
        No one
            must know who you are. There would be no more peace and quiet for you. Go!" </said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"Will I see you again?" </said>
          <said
            aloud="true" direct="true" who="woman" listener="Fridolin">"It's impossible." </said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"Then I shall stay." </said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"My life, at most, is at
        stake,"</said> he said, <said aloud="true" direct="true" who="Fridolin" listener="woman">"and
        I'm ready at this moment to give it for you."</said> He took her hands and tried to draw her
        to him. She whispered again, almost despairingly: <said aloud="true" direct="true"
            who="woman" listener="Fridolin">"Go!" </said> He laughed, and he heard himself laughing
        as in a dream. <said aloud="true" direct="true" who="Fridolin" listener="woman">"But I know
        what I'm doing. You are not all
            here just to make us mad by looking at you. You are doing this to unnerve me still
            more." </said>
          <said aloud="true" direct="true" who="woman" listener="Fridolin">"It will
        soon
            be too late. You must go!" </said> But he wouldn't listen to her. <said aloud="true"
            direct="true" who="Fridolin" listener="woman">"Do you mean to say that there are no
            rooms here for the convenience
            of congenial couples? Will all these people leave with just a courteous 'good-bye'? They
        don't look like
            it." </said> He pointed to the dancers, glowing white bodies closely pressed against the
        blue, red and yellow silk of their partners, circling, in the brilliant, mirrored room
        adjoining, to the wild tunes of the piano. It seemed to him that no longer was any attention
        paid to him and the woman beside him. They stood alone in the semi-dark middle room. <said
            aloud="true" direct="true" who="woman" listener="Fridolin">"You are hoping in vain,"</said>
        she whispered. <said aloud="true" direct="true" who="woman" listener="Fridolin">"There are
            no such rooms here. This is your last opportunity
            to leave." </said>
          <said aloud="true" direct="true" who="Fridolin" listener="woman">"Come
        with me!" </said> She shook her head violently, despairingly. .. He laughed again, not
        recognizing his laughter. <said aloud="true" direct="true" who="Fridolin" listener="woman">"You're
        making game of me. Did all these men and
            women come here merely to fan the flames of their desire and then depart? Who can forbid
        you to
            come away with me if you choose?" </said> She took a deep breath and drooped her head. <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"Oh, now I understand,"</said>
        he said. <said aloud="true" direct="true" who="Fridolin" listener="woman">"That's the
        punishment you impose on those who come here
            uninvited. You couldn't have invented a more cruel one. Please let me off and forgive
            me. Impose some
            other penalty, anything but that I must leave you."</said>
          <said aloud="true"
            direct="true" who="woman" listener="Fridolin">"You are mad. I can't go with you, let
        alone anyone else. Whomever I went with would forfeit his life
            and mine." </said>
          <rs ref="#Fridolin" type="character">Fridolin</rs> felt intoxicated,
        not only with her, her fragrant body and her red-glowing mouth—not only with the atmosphere
        of this room and the voluptuous mysteries that surrounded him—he was intoxicated, his thirst
        unsatisfied, with all the experiences of the night, none of which had come to a satisfactory
        conclusion. He was intoxicated with himself, with his boldness, the change he felt in
        himself, and he touched the veil which was wound about her head, as though he intended to
        remove it. She seized his hands. <said aloud="true" direct="true" who="woman"
            listener="Fridolin">"One night during the dance here one of the men took it into his
            head to tear the
            veil from one of us. They ripped the mask from his face and drove him out with whips." </said>
          <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"And—she?"</said> 
          <said
            aloud="true" direct="true" who="woman" listener="Fridolin">"Did you read of a beautiful
        young girl, only a few weeks ago, who took poison the day before her
            wedding?" </said> He remembered the incident, even the name, and mentioned it. <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"Wasn't it a girl of the
        nobility who
            was engaged to marry an Italian Prince?" </said> She nodded. One of the cavaliers, the
        most distinguished looking of them all and the only one dressed in white, suddenly stopped
        before them. With a slight bow, courteous but imperative, he asked the woman with whom <rs
            ref="#Fridolin" type="character">Fridolin</rs> was talking to dance with him. She seemed
        to hesitate a moment, but he put his arm around her waist and they drifted away to join the
        other couples in the adjoining room. A sudden feeling of solitude made <rs ref="#Fridolin"
            type="character">Fridolin</rs> shiver as if with cold. He looked about him. Nobody
        seemed to be paying any attention to him. This was perhaps his last chance to leave with
        impunity. He didn't know, however, why it was that he remained spell-bound in his corner
        where he now felt sure that he was not observed. It might be his aversion to an inglorious
        and perhaps ridiculous retreat, or the excruciating ungratified desire for the beautiful
        woman whose fragrance was still in his nostrils. Or he may have stayed because he vaguely
        hoped that all that had happened so far was intended as a test of his courage and that this
        magnificent woman would be his reward. It was clear at any rate that the strain was too
        great to be endured, and that, no matter what the danger, he would have to end it. It could
        hardly cost him his life, no matter what he decided. He might be among fools, or libertines,
        but certainly not among rascals or criminals. The thought occurred to him to acknowledge
        himself as an intruder and to place himself at their disposal in chivalrous fashion. This
        night could only conclude in such a manner,—with a harmonious finale, as it were—if it were
        to mean more than a wild, shadow-like succession of gloomy and lascivious adventures, all
        without an end. So, taking a deep breath, he prepared to carry out his plan. At this moment,
        however, a voice whispered beside him: <said aloud="true" direct="true" who="cavalier"
            listener="Fridolin">"Password!"</said> A <rs ref="#cavalier" type="character">cavalier</rs>
        in black had stepped up to him unseen. As <rs ref="#Fridolin" type="character">Fridolin</rs>
        didn't reply, he repeated his question. <said aloud="true" direct="true" who="Fridolin"
            listener="cavalier">"Denmark,"</said> said <rs ref="#Fridolin" type="character">Fridolin</rs>
        . <said aloud="true" direct="true" who="cavalier" listener="Fridolin">"That's
            right, sir, that's the password for admittance, but what's the password of the house,
            may I
            ask?"</said> <rs ref="#Fridolin" type="character">Fridolin</rs> was silent. <said
            aloud="true" direct="true" who="cavalier" listener="Fridolin">"Won't you be kind enough
        to tell me the password of the house?"</said> It sounded like a sharp threat. <rs
            ref="#Fridolin" type="character">Fridolin</rs> shrugged his shoulders. The other walked
        to the middle of the room and raised his hand. The piano ceased playing and the dance
        stopped. Two other cavaliers, one in yellow, the other in red, stepped up. <said
            aloud="true" direct="true" who="cavaliers" listener="Fridolin">"The password, sir,"</said>
        they said simultaneously. <said aloud="true" direct="true" who="Fridolin"
            listener="cavalier">"I have forgotten it,"</said> replied <rs ref="#Fridolin"
            type="character">Fridolin</rs> with a vacant smile but feeling quite calm. <said
            aloud="true" direct="true" who="YellowGentlemen" listener="Fridolin">"That's
        unfortunate,"</said> said the <rs ref="YellowGentlemen" type="character">gentleman</rs> in
        yellow, <said aloud="true" direct="true" who="YellowGentlemen" listener="Fridolin">"for here
        it doesn't matter whether you have
            forgotten it or if you never knew it." </said> The other men flocked in and the doors on
        both sides were closed. <rs ref="#Fridolin" type="character">Fridolin</rs> stood alone in
        the garb of a monk in the midst of the gay-colored cavaliers. <said aloud="true"
            direct="true" who="gentlemen" listener="Fridolin">"Take off your mask!"</said> several
        of them demanded. <rs ref="#Fridolin" type="character">Fridolin</rs> held out his arm to
        protect himself. It seemed a thousand times worse to be the only one unmasked amongst so
        many that were, than to stand suddenly naked amongst people who were dressed. He replied
        firmly: <said aloud="true" direct="true" who="Fridolin" listener="gentlemen">"If my
        appearance here has
            offended any of the gentlemen present, I am ready to give satisfaction in the usual
        manner, but I shall
            take off my mask only if all of you will do the same." </said>
          <said aloud="true"
            direct="true" who="RedCavalier" listener="Fridolin">"It's not a question of
        satisfaction,"</said> said the <rs ref="RedCavalier" type="character">cavalier</rs> in red,
        who until now had not spoken, <said aloud="true" direct="true" who="RedCavalier"
            listener="Fridolin">"but one of
            expiation." </said>
          <said aloud="true" direct="true" who="unkown" listener="Fridolin">"Take
        off your mask!"</said> commanded another in a high-pitched, insolent voice which reminded <rs
            ref="#Fridolin" type="character">Fridolin</rs> of an officer giving orders, <said
            aloud="true" direct="true" who="unkown" listener="Fridolin">"and we'll tell you to your
        face what's in store for you." </said>
          <said aloud="true" direct="true" who="Fridolin"
            listener="gentlemen">"I shall not take it off,"</said> said <rs ref="#Fridolin"
            type="character">Fridolin</rs> in an even sharper tone, <said aloud="true" direct="true"
            who="Fridolin" listener="gentlemen">"and woe to him who dares to touch me." </said> A
        hand suddenly reached out, as if to tear off the mask, when a door suddenly opened and one
        of the women—<rs ref="#Fridolin" type="character">Fridolin</rs> did not doubt which one it
        was—stood there, dressed as a nun, as he had first seen her. The others could be seen behind
        her in the brilliantly lighted room, naked, with veiled faces, crowding together in a
        terrified group. The door at once closed again. <said aloud="true" direct="true" who="woman"
            listener="gentlemen">"Leave him alone,"</said> said the <rs ref="woman" type="character">
        nun</rs>. <said aloud="true" direct="true" who="woman" listener="gentlemen">"I am ready to
        redeem him."</said> There was a short, deep silence, as though something monstrous had
        happened. The <rs ref="cavalier" type="character">cavalier </rs>in black who had first
        demanded the password from <rs ref="#Fridolin" type="character">Fridolin</rs> turned to the
        nun, saying: <said aloud="true" direct="true" who="cavaliers" listener="Fridolin">"You know
        what you are
            taking upon yourself in doing this." </said>
          <said aloud="true" direct="true"
            who="Fridolin" listener="cavalier">"I know." </said> There was a general sigh of relief
        from those present. <said aloud="true" direct="true" who="cavalier" listener="Fridolin">"You
        are free,"</said> said the <rs ref="cavalier" type="character">cavalier </rs> to <rs
            ref="#Fridolin"
            type="character">Fridolin</rs>. <said aloud="true" direct="true" who="cavaliers"
            listener="Fridolin">"Leave this house at once and be careful not to inquire
            further into what you have seen here. If you attempt to put anyone on our trail, whether
        you succeed or
            not—you will be doomed." </said>
          <rs ref="#Fridolin" type="character">Fridolin</rs> stood
        motionless. <said aloud="true" direct="true" who="Fridolin" listener="gentlemen">"How is
            this woman—to redeem me?"</said> he asked. There was no answer. Hands pointed to the
        door indicated that he must go. <rs ref="#Fridolin" type="character">Fridolin</rs> shook his
        head. <said aloud="true" direct="true" who="Fridolin" listener="gentlemen">"Impose what
        punishment you wish, gentlemen, I won't let this woman pay
            for me." </said>
          <said aloud="true" direct="true" who="cavalier" listener="Fridolin">"You
        would be unable, in any case, to change her lot,"</said> the <rs ref="cavalier"
            type="character">cavalier </rs> in black said very gently. <said aloud="true"
            direct="true"
            who="cavalier" listener="Fridolin">"When a
            promise has been made here there is no turning back."</said> The <rs ref="woman"
            type="character">nun</rs> slowly nodded, as if to confirm the statement. <said
            aloud="true" direct="true" who="woman" listener="Fridolin">"Go!"</said> she said to <rs
            ref="#Fridolin" type="character">Fridolin</rs>. <said aloud="true" direct="true"
            who="Fridolin" listener="woman">"No,"</said> replied the latter, elevating his voice. <said
            aloud="true" direct="true" who="Fridolin" listener="woman">"Life means nothing to me if
            I must leave here without
            you. I shall not ask who you are or where you come from. What difference can it make to
        you,
            gentlemen, whether or not you keep up this carnival comedy, though it may aim at a
        serious conclusion.
            Whoever you may be, you surely lead other lives. I won't play a part, here or elsewhere,
        and if I have
            been forced to do so up to now, I shall give it up. I feel that a fate has overtaken me
        which has nothing to
            do with this foolery. I will tell you my name, take off my mask and be responsible for
        the consequences." </said>
          <said aloud="true" direct="true" who="woman" listener="Fridolin">"Don't
        do it,"</said> exclaimed the <rs ref="woman" type="character">nun</rs>, <said aloud="true"
            direct="true" who="woman" listener="Fridolin">"you would only ruin yourself without
        saving me. Go!"</said> Then she turned to the others, saying: <said aloud="true"
            direct="true" who="woman" listener="gentlemen">"Here I am, take me—all of you!"</said>
        The dark costume dropped from her, as if by magic. She stood there in the radiance of her
        white body; reached for the veil which was wrapped about her head, face and neck and unwound
        it with a wonderful circular motion. It sank to the floor, dark hair fell in great profusion
        over her shoulders, breasts and hips—but before <rs ref="#Fridolin" type="character">
        Fridolin</rs> could even glance at her face, he was seized by irresistible arms, and pushed
        to the door. A moment later he found himself in the anteroom, the door closed behind him. A
        masked servant brought him his fur coat and helped him put it on. The main door opened
        automatically, and as if driven by some invisible force, he hurried out. As he stood on the
        street the light behind disappeared. The house stood there in silence with closed windows
        from which not a glimmer issued. I must remember everything clearly, was his main thought; I
        must find the house again—the rest will follow as a matter of course. Darkness surrounded
        him. The dull reddish glow of a street lamp was visible a slight distance above where the
        cab was to wait for him. The mourning-coach drove up from the street below, as though he had
        called it. A servant opened the door.</p>
        <p>
          <said aloud="true" direct="true" who="Fridolin" listener="servant">"I have my own cab,"</said>
        said <rs ref="#Fridolin" type="character">Fridolin</rs>. When the servant shook his head, <rs
            ref="#Fridolin" type="character">Fridolin</rs> continued: <said aloud="true"
            direct="true" who="Fridolin" listener="servant">"If it has
            already gone, I'll walk back to the city." </said> The man replied with a wave of his
        hand which was anything but servant-like, so that objection was out of the question. The
        ridiculously high silk hat of the coachman towered up into the night. The wind was blowing a
        gale; violet clouds raced across the sky. <rs ref="#Fridolin" type="character">Fridolin</rs>
        felt that, after his previous experience, there was nothing for him to do but to get into
        the carriage. It started the moment he was inside. He resolved, as soon as possible, to
        clear up the mystery of his adventure, no matter how dangerous it might be. His life, it
        seemed, would not have the slightest meaning any more, if he did not succeed in finding the
        incomprehensible <rs ref="woman" type="character">woman</rs> who at this very moment was
        paying for his safety. It was only too easy to guess the price. But why should she sacrifice
        herself for him? To sacrifice—? Was she the kind of woman to whom the things that were
        facing her, that she was now submitting to, could mean a sacrifice? If she attended these
        affairs—and since she seemed to understand the rules so well it could not be her first
        time—what difference could it make to her if she belonged to one of the cavaliers, or to
        all? Indeed, could she possibly be anything but a woman of easy virtue? Were any of them
        anything else? That's what they were, without a doubt, even if all of them led another, more
        normal life, so to speak, besides this one of promiscuity. Perhaps everything he had just
        gone through had been only an outrageous joke. A joke planned, prepared and even rehearsed
        for such an occasion when some bold outsider should be caught intruding? And yet, as he
        thought of the <rs ref="woman" type="character">woman</rs> who had warned him from the very
        beginning, who was now ready to pay for him—he remembered something in her voice, her
        bearing, in the royal nobility of her nude body which could not possibly have been false. Or
        was it possible that only his sudden appearance had caused her to change? After everything
        that had happened, such a supposition did not seem impossible. There was no conceit in this
        idea. There may be hours or nights, he thought, in which some strange, irresistible charm
        emanates from men who under normal circumstances have no special power over the other sex.
        The carriage continued up-hill. If all were well, he should have turned into the main street
        long ago. What were they going to do with him? Where was the carriage taking him? Was the
        comedy to be continued elsewhere? And what would the continuation be? A solution of the
        mystery and a happy reunion at some other place. Would he be rewarded for passing the test
        so creditably and made a member of the secret society? Was he to have unchallenged
        possession of the lovely nun? </p>
        <p> The windows of the carriage were closed and <rs
            ref="#Fridolin" type="character">Fridolin</rs> tried to look out—but they were opaque.
        He attempted to open them, first on one side, then on the other, but it was impossible. The
        glass partition between him and the coachman's box was just as thick and just as firmly
        closed. He knocked on the glass, he called, he shouted, but the carriage went on. He tried
        to open both the doors, but they wouldn't budge. His renewed calling was drowned by the
        rattling of the wheels and the roaring of the wind. The carriage began to jolt, going
        down-hill, faster and faster. <rs ref="#Fridolin" type="character">Fridolin</rs>, uneasy and
        alarmed, was on the point of smashing one of the blind windows, when the carriage suddenly
        stopped. Both doors opened together, as if by some mechanism, and as though <rs
            ref="#Fridolin" type="character">Fridolin</rs> had been ironically given the choice
        between one side or the other. He jumped out, the doors closed with a bang—and without the
        coachman paying the slightest attention to him, the carriage drove away across the open
        field into the darkness of the night. The sky was overcast, clouds raced across it, and the
        wind whistled. <rs ref="#Fridolin" type="character">Fridolin</rs> stood in the snow which
        shed a faint light round about. He was alone, his open fur coat over his monk's costume, the
        pilgrim's hat on his head; and an uncanny feeling overcame him. The main street was a slight
        distance away, where a row of dimly-flickering street lamps indicated the direction of the
        city. However, he ran straight down across the sloping, snow-covered field, which shortened
        the way, so as to get among people as quickly as possible. His feet soaked, he came into a
        narrow, almost unlighted street, and at first walked along between high board fences which
        groaned in the wind. Turning the next corner, he reached a somewhat wider street, where
        scattered little houses alternated with empty building lots. Somewhere a tower clock struck
        three. </p>
        <p> Someone was coming towards him. The person wore a short jacket, he had his
        hands in his trouser pockets, his head was down between his shoulders, and his hat was
        pulled over his forehead. <rs ref="#Fridolin" type="character">Fridolin</rs> got ready for
        an attack, but the tramp unexpectedly turned and ran. <said aloud="false" direct="false"
            who="Fridolin" listener="Fridolin">What does that mean?</said> he asked himself. Then he
        decided that he must present a very uncanny appearance, took off the pilgrim's hat and
        buttoned his coat, underneath which the monk's gown was flapping around his ankles. Again he
        turned a corner into a suburban main street. A man in peasant's dress walked past and spoke
        to him, thinking him a priest. The light of a street lamp fell upon a sign on a corner
        house. Liebhartstal—then he wasn't very far from the house which he had left less than an
        hour before. For a second he felt tempted to retrace his steps and to wait in the vicinity
        for further developments. But he gave up the idea when he realized that he would only expose
        himself to grave danger without solving the mystery. As he imagined what was probably taking
        place in the villa at this very moment he was filled with wrath, despair, shame and fear.
        This state of mind was so unbearable that it almost made him sorry the tramp had not
        attacked him; in fact, he almost regretted that he wasn't lying against the fence in the
        deserted street with a knife-gash in his side. That, at least, might have given some
        significance to this senseless night with its childish adventures, all of which had been so
        ruthlessly cut short. It seemed positively ridiculous to return home, as he now intended
        doing. But nothing was lost as yet. There was another day ahead, and he swore that he would
        not rest until he had found again the beautiful <rs ref="woman" type="character">woman</rs>
        whose dazzling nakedness had so intoxicated him. It was only now that he thought of <rs
            ref="Albertina" type="character">Albertina</rs>, but with a feeling that she, too, would
        first have to be won. He could not, must not, be reunited with her until he had deceived her
        with all the other women of the night. With the naked <rs ref="woman" type="character">woman</rs>,
        with <rs ref="Pierrette" type="character">Pierrette</rs>, with <rs ref="Marianne"
            type="character">Marianne</rs>, with <rs ref="Mizzi" type="character">Mizzi</rs> in the
        narrow street. And shouldn't he also try to find the insolent student who had bumped into
        him, so that he might challenge him to a duel with sabres or, better still, with pistols?
        What did someone else's life, what did his own, matter to him? Is one always to stake one's
        life just from a sense of duty or self-sacrifice, and never because of a whim or a passion,
        or simply to match oneself against Fate? Again the thought came to him that even now the
        germ of a fatal disease might be in his body. Wouldn't it be silly to die just because a
        child with diphtheria had coughed in his face? Perhaps he was already ill. Wasn't he
        feverish? Perhaps at this moment he was lying at home in bed—and everything he thought he
        had experienced was merely delirium? </p>
        <p>
          <rs ref="#Fridolin" type="character">Fridolin</rs> opened his eyes as wide as possible,
        passed his hand over his forehead and cheeks and felt his pulse. It scarcely beat faster.
        Everything was all right. He was completely awake. He continued along the street, towards
        the city. A few market-wagons rumbled by, and now and then he met poorly dressed people
        whose day was just beginning. Behind the window of a coffee-house, at a table over which a
        gas-flame flickered, sat a fat man with a scarf around his neck, his head on his hands, fast
        asleep. The houses were still enveloped in darkness, though here and there a few windows
        were lighted and <rs ref="#Fridolin" type="character">Fridolin</rs> thought he could feel
        the people gradually awaking. It seemed that he could see them stretching themselves in
        their beds and preparing for their pitiful and strenuous day. A new day faced him, too, but
        for him it wasn't pitiful and dull. And with a strange, happy beating of his heart, he
        realized that in a few hours he would be walking around between the beds of his patients in
        his white hospital coat. A one-horse cab stood at the next corner, the coachman asleep on
        the box. <rs ref="#Fridolin" type="character">Fridolin</rs> awakened him, gave his address
        and got in. </p> [END ERICA PART 2] </div>
    </body>
"""

# Parse the XML content
root = ET.fromstring(xml_content)

# Dictionary to store interactions between characters
interactions = defaultdict(int)

# Iterate through each <said> element
for said_elem in root.findall('.//said'):
    who = said_elem.get('who')
    listener = said_elem.get('listener')
    
    # Ignore unknown characters
    if who != 'unknown':
        if listener != 'unknown':
            interactions[(who, listener)] += 1
        else:
            interactions[(who, None)] += 1

# Write interactions to a CSV file
with open('interactions.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header
    csvwriter.writerow(['Character', 'Listener', 'Interaction Count'])
    
    # Write data rows
    for (who, listener), count in interactions.items():
        listener_str = listener if listener else "unknown"
        csvwriter.writerow([who, listener_str, count])

print("CSV file 'interactions.csv' created.")
