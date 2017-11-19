class EcoCarGraph{

    constructor(svgName, height, width, newData){
        this.newData = newData;
        this.svgName = svgName;
        this.height = height;
        this.width = width;
        this.limit = 60 * 1;
        this.duration = 750;
        this.now = new Date(Date.now() - this.duration);
        this.svg = d3
                    .select('.' + svgName)
                    .attr('class', 'chart')
                    .attr('width', width)
                    .attr('height', height+50);
        this.x = d3
                .time
                .scale()
                .domain([
                    this.now - (this.limit - 2),
                    this.now - this.duration
                ])
                .range([0, this.width]);
        this.y = d3
                .scale
                .linear()
                .domain([0, 100])
                .range([this.height, 10])

        this.yaxis = this.svg
                .append("g")
                .attr('class', 'y axis')
                .attr("transform", "translate(30,0)")
                .call(this.y.axis = d3.svg.axis().scale(this.y).ticks(6).orient('left'));

        this.groups = {
                current: {
                    value: 0,
                    color: 'black',
                    data: d3
                        .range(this.limit)
                        .map(function () {
                            return 0
                        })
                    }
                };
        
        this.line = d3
                .svg
                .line()
                .interpolate('basis')
                .x((function (d, i) {
                    return this.x(this.now - (this.limit - 1 - i) * this.duration)
                }).bind(this))
                .y((function (d) {
                    return this.y(d)
                }).bind(this));

        this.axis = this.svg
                .append('g')
                .attr('class', 'x axis')
                .attr('class', 'y axis')
                .attr('transform', 'translate(30,' + this.height + ')')
                .call(this.x.axis = d3.svg.axis().scale(this.x).orient('bottom'))
                .call(this.y.axis = d3.svg.axis().scale(this.y).ticks(6).orient('left'));;

        this.paths = this.svg.append('g');

        for (var name in this.groups) {
            var group = this.groups[name]
            group.path = this.paths
                .append('path')
                .data([group.data])
                .attr('class', name + ' group')
                .style('stroke', group.color)
        }

        this.tick = this.tick.bind(this);
    }


    tick() {
        this.now = new Date()

        // Add new values
        for (var name in this.groups) {
            var group = this.groups[name]
            //group.data.push(group.value) // Real values arrive at irregular intervals
            group
                .data
                .push(this.newData())
            this.y.domain([0, d3.max(group.data)]);
            group
                .path
                .attr('d', this.line)
        }

        // Shift domain
        this.x.domain([
            this.now - (this.limit - 2) * this.duration,
            this.now - this.duration
        ])

        // Slide x-axis left
        this.axis
            .transition()
            .duration(this.duration)
            .ease('linear')
            .call(this.x.axis)

        // Adjust the y axis
        this.yaxis.call(this.y.axis = d3.svg.axis().scale(this.y).ticks(6).orient('left'));

        // Slide paths left
        this.paths
            .attr('transform', null)
            .transition()
            .duration(this.duration)
            .ease('linear')
            .attr('transform', 'translate(' + this.x(this.now - (this.limit - 1) * this.duration) + ')')
            .each('end', this.tick)

        // Remove oldest data point from each group
        for (var name in this.groups) {
            var group = this.groups[name]
            group
                .data
                .shift()
        }
    }
}

class EcoCarDisplayData {
    constructor(divName) {
        this.element = document.getElementById(divName);
        this.update = this
            .update
            .bind(this);
    }

    update(data) {
        this.element.innerHTML = data;
    }
}