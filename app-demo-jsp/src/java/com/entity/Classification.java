/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.entity;

import java.io.Serializable;
import java.util.Collection;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.Lob;
import javax.persistence.ManyToMany;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author agno3
 */
@Entity
@Table(name = "classification")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Classification.findAll", query = "SELECT c FROM Classification c")
    , @NamedQuery(name = "Classification.findByClassId", query = "SELECT c FROM Classification c WHERE c.classificationPK.classId = :classId")
    , @NamedQuery(name = "Classification.findByClassImg", query = "SELECT c FROM Classification c WHERE c.classImg = :classImg")
    , @NamedQuery(name = "Classification.findByClassRecommendType", query = "SELECT c FROM Classification c WHERE c.classRecommendType = :classRecommendType")
    , @NamedQuery(name = "Classification.findByClassChooseType", query = "SELECT c FROM Classification c WHERE c.classChooseType = :classChooseType")
    , @NamedQuery(name = "Classification.findByClassEvaluate", query = "SELECT c FROM Classification c WHERE c.classEvaluate = :classEvaluate")
    , @NamedQuery(name = "Classification.findByUserUserId", query = "SELECT c FROM Classification c WHERE c.classificationPK.userUserId = :userUserId")})
public class Classification implements Serializable {

    private static final long serialVersionUID = 1L;
    @EmbeddedId
    protected ClassificationPK classificationPK;
    @Size(max = 200)
    @Column(name = "class_img")
    private String classImg;
    @Column(name = "class_recommend_type")
    private Integer classRecommendType;
    @Column(name = "class_choose_type")
    private Integer classChooseType;
    @Lob
    @Size(max = 65535)
    @Column(name = "class_result")
    private String classResult;
    @Column(name = "class_evaluate")
    private Integer classEvaluate;
    @JoinTable(name = "expert_has_classification", joinColumns = {
        @JoinColumn(name = "classification_user_user_id", referencedColumnName = "user_user_id")
        , @JoinColumn(name = "classification_class_id", referencedColumnName = "class_id")}, inverseJoinColumns = {
        @JoinColumn(name = "expert_expert_id", referencedColumnName = "expert_id")})
    @ManyToMany
    private Collection<Expert> expertCollection;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "classification")
    private Collection<Commodity> commodityCollection;

    public Classification() {
    }

    public Classification(ClassificationPK classificationPK) {
        this.classificationPK = classificationPK;
    }

    public Classification(String classId, int userUserId) {
        this.classificationPK = new ClassificationPK(classId, userUserId);
    }

    public ClassificationPK getClassificationPK() {
        return classificationPK;
    }

    public void setClassificationPK(ClassificationPK classificationPK) {
        this.classificationPK = classificationPK;
    }

    public String getClassImg() {
        return classImg;
    }

    public void setClassImg(String classImg) {
        this.classImg = classImg;
    }

    public Integer getClassRecommendType() {
        return classRecommendType;
    }

    public void setClassRecommendType(Integer classRecommendType) {
        this.classRecommendType = classRecommendType;
    }

    public Integer getClassChooseType() {
        return classChooseType;
    }

    public void setClassChooseType(Integer classChooseType) {
        this.classChooseType = classChooseType;
    }

    public String getClassResult() {
        return classResult;
    }

    public void setClassResult(String classResult) {
        this.classResult = classResult;
    }

    public Integer getClassEvaluate() {
        return classEvaluate;
    }

    public void setClassEvaluate(Integer classEvaluate) {
        this.classEvaluate = classEvaluate;
    }

    @XmlTransient
    public Collection<Expert> getExpertCollection() {
        return expertCollection;
    }

    public void setExpertCollection(Collection<Expert> expertCollection) {
        this.expertCollection = expertCollection;
    }

    @XmlTransient
    public Collection<Commodity> getCommodityCollection() {
        return commodityCollection;
    }

    public void setCommodityCollection(Collection<Commodity> commodityCollection) {
        this.commodityCollection = commodityCollection;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (classificationPK != null ? classificationPK.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Classification)) {
            return false;
        }
        Classification other = (Classification) object;
        if ((this.classificationPK == null && other.classificationPK != null) || (this.classificationPK != null && !this.classificationPK.equals(other.classificationPK))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.Classification[ classificationPK=" + classificationPK + " ]";
    }
    
}
