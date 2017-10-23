# Mock-Trial-Calculations

The following program is a GUI application, written in Python and targeting the Windows platform. It's purpose is to allow AMTA competitors to calculate a relative "individual score" for accurate comparisons across competitors. With a normalization to allow comparison of competitors with different numbers of scores on a given ballot. 
### About

In the past, determining who did the best on a given team, or even simple efficacy and contribution of individual competitors as a part of the team, was an entirely subjective exercise. However, my coach, Marshall Gardener, has come up with a system for using the AMTA ballot's to mathematically calculate each team members contribution. I then took it upon myself to make this methodology accessable to anyone through an easy to use GUI, and applicable to anyone by normalizing the scores over how many chances each person had to earn points on a given ballot.
The underlying system can be found rather easily in the source code, which I have obviousy made open and avalible, but the main benefits of this application will include:

* a GUI method of input for ballot scores.
* a GUI for choosing your roles.
* The ability to store more than one ballot for calculations and select roles on a per ballot basis.

Goals for further development include but are not limited to:

* The ability to rerun over the same ballot multiple time, so as to be able run the calculations for multiple competitors without having to reinput the underlying data
* The ability to save your ballot data to a unique, easy to load format, allowing users to rerun over old tourny result, add new results to the old, and create running totals of perfromance to date.

### Version

0.0.0

**Notice:** This application is prerelease version 0, the development process will continue to be pushed to github, but version numbers will not begin to increase until I feel the intial work has been updated in a satisfactory matter such that the previous work posted defined a distinct version. When I feel the program is ready for public release I will instance the version number to 1.0.0 and begin releasing executable files for supported OSes. While prerelease development will likely be rapid, it is both irresponsible and legally unfounded to take any release notes, blog posts, social media updates, or other statements of authors or contributors as a contract implying a set date of completion or legal deadlines of any kind.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and end user cases.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

**If you are visiting early enough in prerelease to see this message, please know that the below is template space filler and will be replaced once a viable development release candidate has been posted.**

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Built With

* [Atom](https://atom.io/) - The IDE used in primary development
* [Python 3.6.3](https://www.python.org/downloads/release/python-363/) - The development language and interpreter

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Jacob Ferguson** - *Initial work* - [Zomban](https://github.com/zomban)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Special thanks to Marshall Gardener, as his techiniques for aquiring scores was used as the base for this program, credit for the use of the average scores of opposing directs to help calculate point gaps a given competitor is responsible for.
* Acknoledgements to [AMTA](http://www.collegemocktrial.org/), for providing the offical rules of judging torunaments, as well as the system of ballots. 
