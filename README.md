# met-museum-collection
<p>Using The Met's <a href="https://github.com/metmuseum/openaccess">Open Access</a> data, this project looks for differences between the Met's full dataset and the subset of works marked "Is Highlight." I would like to thank the museum for making their data publicly available. The version of the dataset that I downloaded was last updated in September of 2022, but I accessed it on March 10, 2023.</p>

<h2>General Collection Findings</h2>
<ul>
<li>As of March 10, 2023, there were 477,804 works in the dataset.</li>
<li>43.09% of thoe works are unattributed to any artist.</li>
<li>The artist with the most works in the dataset was Walker Evans, with 7,505 attributed works.</li>
<li>For works for which the Artist Nationality field had a value, 24.6% were by American Artists.</li>
<li>For works for which the Culture field had a vlaue, the most represented culture was American, then French, then Greek/Attic.</li>
<li>The department with the most works in the dataset was Drawings and Prints, with 167,152 works, or 34.98% of works in the dataset.</li>
<li>For works with a Classification, most were labeled "Prints."</li>
<li>The department with the least works in the dataset was The Library, with 390 works, or 0.08% of the full dataset.</li>
</ul>

<h2>Highlights Collection Findings</h2>
<ul>
<li>As of March 10, 2023, there were 2,484 works marked "Is Highlight" in the dataset.</li>
<li>27.81% of highlighted works were unattributed to any artist.</li>
<li>The artists with the most highlighted works—12 each—were Winslow Homer and John Singer Sargent.</li>
<li>391 out of 1,692 works with an Artist Nationality were by American artists—23.1%</li>
<li>17.47% of highlighted works belong to The American Wing, but only 2.36% of works in the American Wing were considered highlights.</li>
<li>The department with the highest share of highlighted works was The Library, which was made up of 96.41% highlighted works.</li>
<li>For works with a Classification, most were labeled paintings—262, or 14.64%. Only 49, or 2.74% were prints.</li>
</ul>

<h2>Comparing the Collections</h2>
<ul>
<li>0.52% of all works in the dataset were considered highlights.</li>
<li>27.81% of highlighted works were by an unknown artist—a statistically significant departure from the trend in the overall dataset.</li>
<li>1.71% of all works in the dataset were classified as paintings, but more than 14.64% (considering some departments use the medium field, in lieu of the classificaiton field) of highlighted works were marked "Paintings"—this is another statistically significant difference from the overall dataset. </li>
<li>Though "American" was the most common nationality in both the highlighted subset and the overall dataset, the share of works by American artists considered highlights was actually smaller than the share of American artists overall—though not to a statistically significant degree.</li>
</ul>


<h2>Conclusions</h2>
<p>Please keep in mind that these conclusions are based on correlation, not causation:</p>
<ul>
<li>The Met highlighted works by known artists at a higher rate than than works by Unkown artists—N.B. It's the business of a museum to teach and share knowledge, so it makes sense to me that the share of highlighted works that can be attributed to named artists is larger in the highlighted subset than in the full dataset. If we know less about the artist, it follows that we likely know less about the object—I also hypothesize that most works by unknown artists are also probably older (Ancient Greek/Attic, for example), meaning the museum may have fewer records and archival materials to draw from pertaining to those works. It is also possible that many of the works by unknown artists are by groups traditionally underrepresented in museum collections, for example women and gender nonconforming individuals (unfortunately, though the Met keeps track of artist gender, the data were malforemed). That is, the smaller share of highlighted works by unknown artists may be due to a lack of resources or historical attention. However, since works by unknown artists make up over a quarter of highlighted works, the museum seems to be making a concerted effort to highlight works by unknown artists. That said, more information is needed in this area to draw a real conclusion (see below).</li>
<li>The Met highlights works with the medium "oil on canvas" at a hgiher rate than works in other media.</li>
<li>Though the department with the most highlighted works is The American Wing, the share of highlighted works by American artists was slightly smaller than the share in the general collection.</li>
<li>Based on the conclusions above, it is likely that works in The American Wing are highlighted at a higher rate because the American Wing has more works by known artists than the general collection (64% vs. 57.67% overall) and more oil on canvas works than the general collection (5.28% vs. 0.72% overall, vs. 11% in the highlights collection).</li>
</ul>


<h2>Assumptions and Questions for Further Inquiry</h2>
<p>I found it interesting that the Met highlighted oil paintings at such a high rate compared to other media. That particular finding brought up a few questions that may aid in a better understanding of what the Met deems a "highlight."</p>
<h3>Assumptions</h3>
<ul>
<li>This project assumes that all works in the dataset are treated as equal—that is, since this dataset does not house data on every object in the Met's collection, it is likely that the musem has prioritized digitizing the metadata according to some internal criteria. For example, perhaps the metadata for the highlighted subset is complete but the general collections dataset is not. That would be relevant information!</li>
<li>This project assumes that each department inputting metadata uses the same definitions for each field—however, over the course of the analysis, it became clear that the different departments use different fields. For example, The American Wing does not have any works with an artwork classification—the works belonging to this department only have values for the medium field, which is more specific.</li>
<li>Furthermore, this project assumes that each department inputting metadata uses the same definition for "Is Highlight." "Highlight" seems subjective—it could have to do with museum patron feedback, curatorial context, acquisition and provenance history, or other criteria that is not made clear in the dataset. Evidence that "Is Highlight" may be interpreted differently by distinct departments is the fact that the Library is made up of over 95% highlighted works, which is anomalous.</li>
</ul>
<h3>Questions</h3> 
<ul>
<li>What considerations does the museum take into account when sending works to one department or another? For example, a print by an American artist—in what instance would the work go to The American Wing vs. Prints and Drawings?</li>
<li>Many wokrs in the Met's collection are not accounted for in the dataset. How does the museum prioritize which are included when? Is the work ongoing?</li>
<li>Do different departments at the museum keep track of different metadata? Do they have different definitions for the metadata?</li>
<li>How does the museum decide which works are highlights? Is there strict criteria, or is the designation more at the department's discretion?</li>
</ul>

<h2>Acknowledgements</h2>
<p>Thank you to the Metropolitan Museum of Art for making these data publicly available.</p>
